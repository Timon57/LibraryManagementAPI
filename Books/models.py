from django.db import models

# User Model
class User(models.Model):
    UserID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=250)
    Email = models.EmailField(unique=True)
    MemberShipDate = models.DateField()

# Book Model
class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=250)
    ISBN = models.CharField(max_length=20)
    PublishedDate = models.DateField()
    Genre = models.CharField(max_length=250)

# BookDetails Model
class BookDetails(models.Model):
    DetailsID = models.AutoField(primary_key=True)
    BookID = models.OneToOneField(Book, on_delete=models.CASCADE,related_name='bookdetails') # 1 to 1 relationship with book
    NumberOfPages = models.IntegerField(null=True, blank=True)
    Publisher = models.CharField(max_length=250,null=True, blank=True)
    Language = models.CharField(max_length=50,null=True, blank=True)

# BorrowedBooks Model
class BorrowedBooks(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE) # 1 to many relationship with user
    BookID = models.ForeignKey(Book, on_delete=models.CASCADE) # 1 to many relationship with book
    BorrowDate = models.DateField()
    ReturnDate = models.DateField(null=True, blank=True)