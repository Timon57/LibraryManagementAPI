from django.shortcuts import render,get_object_or_404
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import ObjectDoesNotExist


@api_view(['GET'])
def users_list(reqeust):
    users = User.objects.all()
    serializer = UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user(request, user_id):
    user = get_object_or_404(User, UserID=user_id)
    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Book APIs
@api_view(['POST'])
def add_new_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_all_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_book(request, book_id):
    book = get_object_or_404(Book, BookID=book_id)
    serializer = BookSerializer(book)
    return Response(serializer.data)



@api_view(['PUT'])
def update_book_details(request, book_id):
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
    serializer = BorrowedBooksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def return_book(request, borrowed_book_id):
    borrowed_book = get_object_or_404(BorrowedBooks, id=borrowed_book_id)
    borrowed_book.return_date = request.data.get('return_date')
    borrowed_book.save()
    return Response({'message': 'Book returned successfully'})

@api_view(['GET'])
def list_all_borrowed_books(request):
    borrowed_books = BorrowedBooks.objects.all()
    serializer = BorrowedBooksSerializer(borrowed_books, many=True)
    return Response(serializer.data)