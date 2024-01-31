from django.db import models

class User(models.Model):
    UserID = models.IntegerField(primary_key=True)
    Name = models.CharField(max_length=250)
    Email = models.EmailField(unique=True)
    MemberShipDate = models.DateField()

class Book(models.Model):
    BookID = models.IntegerField(primary_key=True)
    Title = models.CharField(max_length=250)
    ISBN = models.CharField(max_length=20)
    PublishedDate = models.DateField()
    Genre = models.CharField(max_length=250)

class BookDetails(models.Model):
    DetailsID = models.IntegerField(primary_key=True)
    BookID = models.OneToOneField(Book, on_delete=models.CASCADE)
    NumberOfPages = models.IntegerField()
    Publisher = models.CharField(max_length=250)
    Language = models.CharField(max_length=50)

class BorrowedBooks(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    BookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    BorrowDate = models.DateField()
    ReturnDate = models.DateField(null=True, blank=True)