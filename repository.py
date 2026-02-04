# repository.py
from typing import Dict, List, Optional
from models import Book, Member, Loan


class InMemoryBookRepository:
    """Simple in-memory repository for books."""

    def __init__(self):
        self._books: Dict[str, Book] = {}

    def add(self, book: Book):
        self._books[book.get_id()] = book

    def get(self, book_id: str) -> Optional[Book]:
        return self._books.get(book_id)

    def remove(self, book_id: str):
        if book_id in self._books:
            del self._books[book_id]

    def list_all(self) -> List[Book]:
        return list(self._books.values())


class InMemoryMemberRepository:
    """Simple in-memory repository for members."""

    def __init__(self):
        self._members: Dict[str, Member] = {}

    def add(self, member: Member):
        self._members[member.get_id()] = member

    def get(self, member_id: str) -> Optional[Member]:
        return self._members.get(member_id)

    def list_all(self) -> List[Member]:
        return list(self._members.values())


class InMemoryLoanRepository:
    """Repository for loan records."""

    def __init__(self):
        self._loans: Dict[str, Loan] = {}

    def add(self, loan: Loan):
        self._loans[loan.loan_id] = loan

    def get(self, loan_id: str) -> Optional[Loan]:
        return self._loans.get(loan_id)

    def list_all(self) -> List[Loan]:
        return list(self._loans.values())

    def list_active_loans(self) -> List[Loan]:
        return [loan for loan in self._loans.values() if not loan.returned]

    def list_loans_by_member(self, member_id: str) -> List[Loan]:
        return [
            loan for loan in self._loans.values()
            if loan.member.get_id() == member_id and not loan.returned
        ]
