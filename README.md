# Expense Tracker (CLI)

## Description
A command-line based expense tracking system built in Python.

This project allows users to manage expenses with features like:
- Adding, editing, and deleting expenses
- Filtering and sorting expenses with a generic, chainable system
- Calculating totals dynamically using a flexible query-like system
- Persistent storage using JSON

The goal of this project is to practice object-oriented design, data handling, and building reusable logic similar to real-world backend systems.

## Features
Features:
- Add, edit, and delete expenses
- Filter expenses by:
  - Category
  - Paid by (user)
  - Payment mode
  - Date range
- Sort expenses by amount, category, or date (ascending/descending)
- Combined filter + sort support
-- Calculate totals overall and by filters
  - Overall
  - Based on filters
- Tabular display in CLI
- Data persistence using JSON

## Tech Stack:
- Python
- JSON for storage

## How to Run
1. Clone the repository
2. Navigate to the project folder
3. Run:
python main.py

## Future Improvements
- Database integration (replace JSON with SQL)
- API layer (convert to backend service)
- UI (web or mobile interface)