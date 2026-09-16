# Library Management System

## 1. Project Overview

The Library Management System is a web-based application developed using Django and SQLite.

It helps manage library books through a simple and user-friendly interface. The system allows users to add, view, edit, delete, and search books.

The project also provides a REST API using Django REST Framework.

## 2. Problem Statement

Managing books manually can be time-consuming and may lead to errors.

This system provides a digital solution to manage book information efficiently and makes it easier to search and update library records.

## 3. Objectives

- To develop a web-based Library Management System.
- To implement CRUD operations.
- To store book information in a database.
- To provide REST API endpoints.
- To implement input validation.
- To provide book search functionality.
- To test the application using automated tests.
- To maintain the project using Git and GitHub.

## 4. Technologies Used

- Python
- Django
- Django REST Framework
- HTML
- CSS
- SQLite
- Git
- GitHub
- Visual Studio Code

## 5. Main Features

- Add new books
- View book details
- Edit book details
- Delete books
- Search books
- REST API
- Input validation
- Unique ISBN validation
- Responsive design
- Automated testing
- Django Admin panel

## 6. Book Information

Each book contains:

- Book Title
- Author
- Category
- ISBN
- Available Copies

## 7. CRUD Operations

### Create
Add a new book to the library.

### Read
View all books and individual book details.

### Update
Edit existing book information.

### Delete
Remove a book from the database.

## 8. Search Functionality

The system allows users to search books using:

- Book title
- Author
- Category

## 9. Validation

The system checks:

- Required fields
- Available copies must be a number
- Available copies cannot be negative
- ISBN must be unique

Clear error messages are displayed when invalid data is entered.

## 10. REST API

The project provides REST API endpoints using Django REST Framework.

### Get all books

`GET /api/books/`

### Get one book

`GET /api/books/<id>/`

### Add a book

`POST /api/books/`

### Update a book

`PUT /api/books/<id>/`

### Delete a book

`DELETE /api/books/<id>/`

## 11. Database

SQLite is used as the database.

### Book Table

| Field | Type |
|---|---|
| id | Integer |
| title | String |
| author | String |
| category | String |
| isbn | String |
| available_copies | Integer |

The `isbn` field is unique.

## 12. Project Architecture

```text
User
  |
  v
HTML / CSS Interface
  |
  v
Django Views
  |
  v
Django ORM
  |
  v
SQLite Database

For API requests:

Client
  |
  v
REST API
  |
  v
Django REST Framework
  |
  v
Serializer
  |
  v
SQLite Database

Testing

Automated Django tests were created for:

Book creation
Home page
View book
Edit book
Delete book

The project successfully passed all 5 automated tests.

Installation
Step 1: Clone the repository
git clone https://github.com/Thameemcodespace/Library_Management_System.git

Step 2: Open the project
cd Library_Management_System

Step 3: Create virtual environment
python -m venv venv

Step 4: Activate virtual environment

Windows:
venv\Scripts\activate

Step 5: Install dependencies
pip install django djangorestframework

Step 6: Apply migrations
python manage.py migrate

Step 7: Run the server
python manage.py runserver

Open:
http://127.0.0.1:8000/

Future Enhancements

User authentication
Student/member management
Book issue and return system
Due date tracking
Fine calculation
Dashboard with statistics
Email notifications
Advanced filtering

 Conclusion

The Library Management System provides a simple digital solution for managing library books.

It demonstrates frontend development, Django backend development, database management, REST API development, CRUD operations, validation, testing, and Git/GitHub version control.

## Repository

GitHub Repository:

https://github.com/Thameemcodespace/Library_Management_System

