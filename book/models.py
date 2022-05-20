from django.db import models
from author.models import Author
# Create your models here.
class Book(models.Model):

    BOOKS_CHOICES = [
        ("L", "Libro" ),
        ("R", "Revistas"),
    ]
    FORMAT_CHOICES = [
        ("D", "Digital"),
        ("F", "Libro fisico"),
    ]
    title= models.CharField(max_length=200, blank=False, null=False, default="")
    subject = models.CharField(max_length=200, blank=False, null=False, default="")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    book = models.CharField(choices=BOOKS_CHOICES, max_length=200, default="")
    isbn= models.CharField(max_length=10, primary_key=True, default="")
    publisher = models.CharField(max_length=200, blank=False, null=False, default="")
    language = models.CharField(max_length=200, blank=False, null=False)
    format = models.CharField(choices=FORMAT_CHOICES, max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.isbn} | {self.title} | {self.author.name}" 