from django.shortcuts import render

# Create your views here.
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Expected Output: A Book instance with the specified attributes is created.

book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
# Expected Output: 1984 George Orwell 1949

book.title = "Nineteeen Eighty-Four"
book.save()
# Expected Output: The title of the book is updated to Nineteen Eighty-Four.

book.delete()
# Expected Output: The book is deleted from the database.

books = Book.objects.all()
print(books)
# Expected Output: No books in the queryset, confirming deletion.
