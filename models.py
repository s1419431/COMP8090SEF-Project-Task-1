# models.py
from abc import ABC, abstractmethod
from datetime import date, timedelta
from typing import List, Dict


class Identifiable(ABC):
    """Abstract base class to demonstrate abstraction and polymorphism."""

    @abstractmethod
    def get_id(self) -> str:
        pass


class Person(Identifiable):
    """Base class to demonstrate inheritance."""

    def __init__(self, person_id: str, name: str):
        self._person_id = person_id
        self._name = name

    def get_id(self) -> str:
        return self._person_id

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    def __str__(self) -> str:
        return f"{self._person_id} - {self._name}"


class Member(Person):
    """Library member, derived from Person."""

    def __init__(self, member_id: str, name: str, max_books: int = 5):
        super().__init__(member_id, name)
        self._max_books = max_books
        self._borrowed_book_ids: List[str] = []

    @property
    def max_books(self) -> int:
        return self._max_books

    def can_borrow(self) -> bool:
        return len(self._borrowed_book_ids) < self._max_books

    def borrow_book(self, book_id: str):
        self._borrowed_book_ids.append(book_id)

    def return_book(self, book_id: str):
        if book_id in self._borrowed_book_ids:
            self._borrowed_book_ids.remove(book_id)

    @property
    def borrowed_book_ids(self) -> List[str]:
        # return a copy
        return list(self._borrowed_book_ids)

    def __str__(self) -> str:
        return f"Member({self.get_id()}, {self.name}, borrowed={len(self._borrowed_book_ids)})"


class Book(Identifiable):
    """Book entity."""

    def __init__(self, book_id: str, title: str, author: str, total_copies: int = 1):
        self._book_id = book_id
        self._title = title
        self._author = author
        self._total_copies = total_copies
        self._available_copies = total_copies

    def get_id(self) -> str:
        return self._book_id

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def available_copies(self) -> int:
        return self._available_copies

    def is_available(self) -> bool:
        return self._available_copies > 0

    def borrow_one(self):
        if not self.is_available():
            raise ValueError("No copies available")
        self._available_copies -= 1

    def return_one(self):
        if self._available_copies >= self._total_copies:
            raise ValueError("All copies are already in library")
        self._available_copies += 1

    def __str__(self) -> str:
        return (
            f"Book({self._book_id}, {self._title}, "
            f"{self._author}, available={self._available_copies}/{self._total_copies})"
        )


class Loan:
    """Represents one borrowing record."""

    def __init__(self, loan_id: str, member: Member, book: Book, loan_days: int = 14):
        self._loan_id = loan_id
        self._member = member
        self._book = book
        self._borrow_date = date.today()
        self._due_date = self._borrow_date + timedelta(days=loan_days)
        self._returned: bool = False

    @property
    def loan_id(self) -> str:
        return self._loan_id

    @property
    def member(self) -> Member:
        return self._member

    @property
    def book(self) -> Book:
        return self._book

    @property
    def borrow_date(self) -> date:
        return self._borrow_date

    @property
    def due_date(self) -> date:
        return self._due_date

    @property
    def returned(self) -> bool:
        return self._returned

    def mark_returned(self):
        self._returned = True

    def is_overdue(self) -> bool:
        return (not self._returned) and (date.today() > self._due_date)

    def __str__(self) -> str:
        status = "returned" if self._returned else "active"
        return (
            f"Loan({self._loan_id}, member={self._member.get_id()}, "
            f"book={self._book.get_id()}, due={self._due_date}, {status})"
        )
