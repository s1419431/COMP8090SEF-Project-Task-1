# ui.py
from services import LibraryService


class ConsoleUI:
    """Simple text-based user interface."""

    def __init__(self, service: LibraryService):
        self._service = service

    def run(self):
        while True:
            self._print_menu()
            choice = input("Enter choice: ").strip()
            try:
                if choice == "1":
                    self._handle_add_book()
                elif choice == "2":
                    self._handle_add_member()
                elif choice == "3":
                    self._handle_borrow_book()
                elif choice == "4":
                    self._handle_return_book()
                elif choice == "5":
                    self._handle_list_books()
                elif choice == "6":
                    self._handle_list_members()
                elif choice == "7":
                    self._handle_list_loans()
                elif choice.lower() == "q":
                    print("Goodbye.")
                    break
                else:
                    print("Invalid choice.")
            except Exception as ex:
                print(f"Error: {ex}")

    def _print_menu(self):
        print("\n=== Library Borrowing System ===")
        print("1. Add book")
        print("2. Add member")
        print("3. Borrow book")
        print("4. Return book")
        print("5. List books")
        print("6. List members")
        print("7. List active loans")
        print("Q. Quit")

    def _handle_add_book(self):
        book_id = input("Book ID: ").strip()
        title = input("Title: ").strip()
        author = input("Author: ").strip()
        copies = int(input("Total copies: "))
        self._service.add_book(book_id, title, author, copies)
        print("Book added.")

    def _handle_add_member(self):
        member_id = input("Member ID: ").strip()
        name = input("Name: ").strip()
        max_books = int(input("Max books: "))
        self._service.add_member(member_id, name, max_books)
        print("Member added.")

    def _handle_borrow_book(self):
        member_id = input("Member ID: ").strip()
        book_id = input("Book ID: ").strip()
        loan_days_raw = input("Loan days (default 14): ").strip()
        loan_days = int(loan_days_raw) if loan_days_raw else 14
        loan = self._service.borrow_book(member_id, book_id, loan_days)
        print(f"Loan created: {loan}")

    def _handle_return_book(self):
        member_id = input("Member ID: ").strip()
        book_id = input("Book ID: ").strip()
        loan = self._service.return_book(member_id, book_id)
        if loan:
            print(f"Returned: {loan}")
        else:
            print("No active loan found for this member and book.")

    def _handle_list_books(self):
        books = self._service.list_books()
        print("\n--- Books ---")
        for book in books:
            print(book)

    def _handle_list_members(self):
        members = self._service.list_members()
        print("\n--- Members ---")
        for member in members:
            print(member)

    def _handle_list_loans(self):
        loans = self._service.list_active_loans()
        print("\n--- Active Loans ---")
        for loan in loans:
            print(loan)
