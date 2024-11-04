# Django Book List App

This is a simple Django application for managing a list of books, demonstrating basic CRUD (Create, Read, Update, Delete) operations with Bootstrap 5 styling.

## Features
- List all books in a table format.
- Add new books using a form.
- Edit and update existing books.
- Delete books with a confirmation alert.
- Styled with Bootstrap 5 for a responsive and clean UI.
- `db.sqlite3` The SQLite database file where all data is stored (generated after migrations).

## Requirements
- Python 3.x
- Django
- django-bootstrap-v5

## Database
This project uses **SQLite** as the default database, which is set up automatically when you run migrations. SQLite is a lightweight, file-based database that's suitable for development and testing environments. By default, Django creates an SQLite database file named `db.sqlite3` in project directory.

## Installation
1. **Clone the repository**:  
   `git clone https://github.com/yourusername/book-list-app.git`  
   `cd djangoCrud`

2. **Set up a virtual environment and activate it**:  
   `python -m venv .venv`  
   `source .venv/bin/activate`  *(On Windows use `.venv\Scripts\activate`)*

3. **Install the dependencies**:  
   `pip install django django-bootstrap-v5`

4. **Set up the database**:  
   `python manage.py makemigrations`  
   `python manage.py migrate`

5. **Run the development server**:  
   `python manage.py runserver`

6. **Access the app**: Open your browser and go to `http://127.0.0.1:8000/`.

## Usage
- **View Books**: The homepage displays a list of all books in a table.
- **Add a Book**: Click the "Add Book" button to open a form and add a new book.
- **Edit a Book**: Click the "Edit" button next to a book to modify its details.
- **Delete a Book**: Click the "Delete" button next to a book and confirm the deletion in the popup alert.

## Licence
https://senghuyjr11.surge.sh
