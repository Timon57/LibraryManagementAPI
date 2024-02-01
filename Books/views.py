from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import ObjectDoesNotExist
from .models import User, Book, BookDetails, BorrowedBooks
from .serializers import UserSerializer, BookSerializer, BookDetailsSerializer, BorrowedBooksSerializer

# User APIs

@api_view(['GET'])
def users_list(request):
    """
    Endpoint to retrieve a list of all users in the system.

    Parameters:
    - None

    Returns:
    - Response: List of user details.
    """
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user(request, user_id):
    """
    Endpoint to fetch a user's details using their UserID.

    Parameters:
    - user_id (int): ID of the user.

    Returns:
    - Response: User details.
    """
    user = get_object_or_404(User, UserID=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    """
    Endpoint to add a new user to the system with details like name, email, and membership date.

    Parameters:
    - request.data: User details including name, email, and membership date.

    Returns:
    - Response: Created user details.
    """
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Book APIs

@api_view(['POST'])
def add_new_book(request):
    """
    Endpoint to add a new book record, including title, ISBN, published date, and genre.

    Parameters:
    - request.data: Book details including title, ISBN, published date, and genre.

    Returns:
    - Response: Created book details.
    """
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_all_books(request):
    """
    Endpoint to retrieve a list of all books in the library.

    Parameters:
    - None

    Returns:
    - Response: List of book details.
    """
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_book(request, book_id):
    """
    Endpoint to fetch details of a specific book using its BookID.

    Parameters:
    - book_id (int): ID of the book.

    Returns:
    - Response: Book details.
    """
    book = get_object_or_404(Book, BookID=book_id)
    serializer = BookSerializer(book)
    return Response(serializer.data)

@api_view(['PUT'])
def update_book_details(request, book_id):
    """
    Endpoint to assign details to a book or update existing book details, like the number of pages, publisher, language.

    Parameters:
    - book_id (int): ID of the book.
    - request.data: Book details including number of pages, publisher, language.

    Returns:
    - Response: Updated book details.
    """
    book = get_object_or_404(Book, BookID=book_id)

    # Try to get the existing BookDetails or create a new one
    book_details, created = BookDetails.objects.get_or_create(BookID=book)

    serializer = BookDetailsSerializer(book_details, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# BorrowedBooks APIs

@api_view(['POST'])
def borrow_book(request):
    """
    Endpoint to record the borrowing of a book by linking a user with a book.

    Parameters:
    - request.data: Borrowed book details including UserID, BookID, and BorrowDate.

    Returns:
    - Response: Created borrowed book details.
    """
    serializer = BorrowedBooksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def return_book(request, borrowed_book_id):
    """
    Endpoint to update the system when a book is returned.

    Parameters:
    - borrowed_book_id (int): ID of the borrowed book.
    - request.data: Return details including return_date.

    Returns:
    - Response: Success message.
    """
    borrowed_book = get_object_or_404(BorrowedBooks, id=borrowed_book_id)
    borrowed_book.return_date = request.data.get('return_date')
    borrowed_book.save()
    return Response({'message': 'Book returned successfully'})

@api_view(['GET'])
def list_all_borrowed_books(request):
    """
    Endpoint to list all books currently borrowed from the library.

    Parameters:
    - None

    Returns:
    - Response: List of borrowed book details.
    """
    borrowed_books = BorrowedBooks.objects.all()
    serializer = BorrowedBooksSerializer(borrowed_books, many=True)
    return Response(serializer.data)
