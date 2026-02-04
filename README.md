# Library Borrowing System (COMP8090SEF Task 1)

This is a simple **library borrowing system** implemented in Python to fulfil the Task 1 requirements of the COMP8090SEF course project (OOP-based application development).[file:1]

> Important: You must modify and extend this code to make it your own work and to cover all OOP concepts and project-specific requirements defined by HKMU.[file:1]

## Features

- Manage books (add, list, availability count).
- Manage members (add, list, borrowing limit).
- Borrow and return books with basic validation.
- Track active loans with due dates and overdue detection logic (in code).

The system uses a console-based menu interface.

## OOP Concepts Demonstrated

- **Classes and objects**: `Book`, `Member`, `Loan`, repositories, `LibraryService`, and `ConsoleUI`.
- **Encapsulation**: Private-like attributes (`_field`) with property accessors where appropriate.
- **Inheritance**: `Member` extends `Person`; both implement the `Identifiable` interface-style abstract base class.
- **Abstraction and polymorphism**: `Identifiable` abstract base class with `get_id()` implemented differently in `Book` and `Person` subclasses.
- **Modular design**: Multiple Python files (`models.py`, `repository.py`, `services.py`, `ui.py`, `main.py`) to separate concerns.[file:1]

You should update this section to explicitly match the OOP concepts listed in your Week 3 lecture notes and explain them in your project report.[file:1]

## Project Structure

```text
.
├── main.py          # Entry point
├── models.py        # Entity and abstract classes
├── repository.py    # In-memory repositories
├── services.py      # Business logic / service layer
├── ui.py            # Console UI
└── README.md
