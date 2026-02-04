# main.py
from repository import (
    InMemoryBookRepository,
    InMemoryMemberRepository,
    InMemoryLoanRepository,
)
from services import LibraryService
from ui import ConsoleUI


def bootstrap_sample_data(service: LibraryService):
    """Optional: add some sample books and members."""
    service.add_book("B001", "Clean Code", "Robert C. Martin", 3)
    service.add_book("B002", "Introduction to Algorithms", "Cormen et al.", 2)
    service.add_member("M001", "Alice", 3)
    service.add_member("M002", "Bob", 2)


def main():
    book_repo = InMemoryBookRepository()
    member_repo = InMemoryMemberRepository()
    loan_repo = InMemoryLoanRepository()
    service = LibraryService(book_repo, member_repo, loan_repo)

    bootstrap_sample_data(service)

    ui = ConsoleUI(service)
    ui.run()


if __name__ == "__main__":
    main()
