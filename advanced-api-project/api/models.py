from django.db import models

# Create your models here.
# Represents an author of books.
class Author(models.Model):
    name = models.CharField(max_length=100)
    # The name field stores the author's name

    def __str__(self):
        return self.name
    # Returns the string representation of the author, which is their name.

# Represents a book written by an author.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    # title, publication_year, and author fields for the Book model
    # The author field establishes a many-to-one relationship from Book to Author.
    # Each book is linked to one author, and each author can have multiple books.
    # The related_name 'books' allows accessing a list of books from an Author instance.

    def __str__(self):
        return self.title
    # Returns the string representation of the book, which is its title.