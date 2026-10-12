# Python Login System (CRUD Practice)

A simple command-line login system built with Python to practice file I/O,
dictionaries, and input validation.

## About

This is a learning project to practice CRUD and I/O using Python.
It's a menu-driven program where you can register users, log in, and manage
accounts. Data is stored in a plain text file. **Not secure** — for practice purposes only.

## Features

- **Register** — create a userid and password
- **Login** — authenticate with userid + password
- **Change userid** — rename your account
- **Change password** — update your password (requires current password)
- **Delete account** — permanently remove your account (requires confirmation + password)
- **View all users** — see every registered userid and password

## UX Details

- Consistent `-quit` escape from any prompt
- Confirmation before destructive actions (delete account)
- Clear error messages for invalid input (colons, spaces, empty fields)
- Auto-clear console between screens
- Retry loops instead of crashing on bad input

## How to Run
- Requires Python 3. In a terminal:
- python3 login.py


