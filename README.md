# LibraryManagementAPI
Task work for building library Management System
Download & Setup Instructions :
Before downloading the project, check to make sure you meet the project's requirements.

Clone the project. This will download the GitHub respository files onto your local machine.

git clone https://github.com/divanov11/mumble
Install Dependencies:
pip install -r requirements.txt
Database Migrations:
python manage.py makemigrations
python manage.py migrate
Run the Development Server:
python manage.py runserver


API Documentation

Create a New User:
users/create/
List All Users:
users/
Get User by ID:
users/<int:user_id>/
Add a New Book:
books/add/
List All Books:
books/
Get Book by ID:
books/<int:book_id>/
Assign/Update Book Details:
books/<int:book_id>/update-details/
Borrow a Book:
books/borrow/
Return a Book: 
books/return/<int:borrowed_book_id>/
List All Borrowed Books:
books/borrowed/

