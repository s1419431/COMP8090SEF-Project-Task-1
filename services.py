# services.py
from typing import Optional
from models import Book, Member, Loan
from repository import (
    InMemoryBookRepository,
    InMemoryMemberRepository,
    InMemoryLoanRepository,
)


class LibraryService:
    """Application service layer encapsulating business logic."""

    def __init__(
        self,
        book_repo: InMemoryBookRepository,
        member_repo: InMemoryMemberRepository,
        loan_repo: InMemoryLoanRepository,
    ):
        self._book_repo = book_repo
        self._member_repo = member_repo
        self._loan_repo = loan_repo
        self._next_loan_id = 1

    def _generate_loan_id(self) -> str:
        loan_id = f"L{self._next_loan_id:04d}"
        self._next_loan_id += 1
        return loan_id

    # --- Book management ---

    def add_book(self, book_id: str, title: str, author: str, total_copies: int = 1):
        if self._book_repo.get(book_id) is not None:
            raise ValueError("Book ID already exists")
        book = Book(book_id, title, author, total_copies)
        self._book_repo.add(book)

    def list_books(self):
        return self._book_repo.list_all()

    # --- Member management ---

    def add_member(self, member_id: str, name: str, max_books: int = 5):
        if self._member_repo.get(member_id) is not None:
            raise ValueError("Member ID already exists")
        member = Member(member_id, name, max_books)
        self._member_repo.add(member)

    def list_members(self):
        return self._member_repo.list_all()

    # --- Borrow / return operations ---

    def borrow_book(self, member_id: str, book_id: str, loan_days: int = 14) -> Loan:
        member = self._member_repo.get(member_id)
        if member is None:
            raise ValueError("Member not found")

        book = self._book_repo.get(book_id)
        if book is None:
            raise ValueError("Book not found")

        if not member.can_borrow():
            raise ValueError("Member has reached maximum borrowing limit")

        if not book.is_available():
            raise ValueError("Book has no available copies")

        book.borrow_one()
        member.borrow_book(book_id)
        loan_id = self._generate_loan_id()
        loan = Loan(loan_id, member, book, loan_days)
        self._loan_repo.add(loan)
        return loan

    def return_book(self, member_id: str, book_id: str) -> Optional[Loan]:
        """Return the active loan for a given member and book, if any."""
        loans = self._loan_repo.list_loans_by_member(member_id)
        for loan in loans:
            if loan.book.get_id() == book_id and not loan.returned:
                loan.mark_returned()
                loan.book.return_one()
                loan.member.return_book(book_id)
                return loan
        return None

    def list_active_loans(self):
        return self._loan_repo.list_active_loans()
