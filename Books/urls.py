from django.urls import path
from .import views
urlpatterns = [
     path('users/', views.users_list, name='users-list'),
    path('users/<int:user_id>/', views.get_user, name='get-user'),
    path('users/create/', views.create_user, name='create-user'),

    # Book APIs
    path('books/add/', views.add_new_book, name='add-new-book'),
    path('books/', views.list_all_books, name='list-all-books'),
    path('books/<int:book_id>/', views.get_book, name='get-book'),
    path('books/<int:book_id>/update-details/', views.update_book_details, name='update-book-details'),

    # BorrowedBooks APIs
    path('books/borrow/', views.borrow_book, name='borrow-book'),
    path('books/return/<int:borrowed_book_id>/', views.return_book, name='return-book'),
    path('books/borrowed/', views.list_all_borrowed_books, name='list-all-borrowed-books'),
]
