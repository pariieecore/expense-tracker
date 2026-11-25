# Python Expense Tracker

## About the Project

This is a simple command-line Expense Tracker developed using Python. It helps users record their daily expenses, organize them into categories, and calculate their total spending.

The program uses a CSV file to store expenses permanently, so the data remains available after restarting the application.

## Features

- Add new expenses
- View all expenses
- Filter expenses by category
- Filter expenses by month
- Calculate category-wise spending
- Display grand total
- Find the biggest single expense
- Validate dates and amounts
- Store expenses permanently using CSV

## Categories

- Food
- Travel
- Study
- Bills
- Fun
- Other

## Technologies Used

- Python 3
- CSV Module
- Datetime Module
- OS Module

## How to Run

1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python expense_tracker.py
```

The program will automatically create `expenses.csv` if it does not exist.

## CSV File Format

The expenses are stored in the following format:

```csv
Date,Category,Description,Amount
2026-11-01,Food,Groceries,450
2026-11-02,Travel,Bus fare,80
```

## Concepts Used

- Functions
- While loops
- Conditional statements
- Dictionaries
- CSV file handling
- Input validation
- Exception handling
- Data grouping and calculation

## Learning Outcome

Through this project, I learned how to read and write CSV files, validate user inputs, calculate category-wise totals, filter records, and create a menu-driven Python application.

## Author

Pari Bansal
