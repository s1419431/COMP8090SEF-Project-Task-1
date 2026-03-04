# Library Borrowing System (COMP8090SEF Task 1)

This is a **Library Borrowing system** of COMP8090SEF course project.
- Created by
- Name: WONG Yan-ho, Michael
- Student ID: 14194311

## Features

- Manage books (add, list, availability count).
- Manage members (add, list, borrowing limit).
- Borrow and return books with basic validation.
- Track active loans with due dates and overdue detection logic (in code).

## Project Structure

```text
.
├── main.py          # Entry point
├── models.py        # Entity and abstract classes
├── repository.py    # In-memory repositories
├── services.py      # Business logic / service layer
├── ui.py            # Console UI
└── README.md
