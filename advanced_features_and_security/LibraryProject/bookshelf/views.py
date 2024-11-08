from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.http import HttpResponseForbidden
from .forms import ExampleForm

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

@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'bookshelf/view_book.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Handle form submission to create a book
        pass
    return render(request, 'bookshelf/create_book.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # Handle form submission to edit a book
        pass
    return render(request, 'bookshelf/edit_book.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('bookshelf:book_list')
    return render(request, 'bookshelf/delete_book.html', {'book': book})

def search_books(request):
    query = request.GET.get('query')
    books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'books': books})

def some_view(request):
    form = ExampleForm()
    return render(request, 'bookshelf/form_example.html', {'form': form})