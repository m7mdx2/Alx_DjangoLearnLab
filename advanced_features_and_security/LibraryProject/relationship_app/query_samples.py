from relationship_app.models import Author, Book, Library, Librarian

# Create an Author object
author = Author(name='J.K. Rowling')
author.save()

# Create a Book object
book = Book(title='Harry Potter', author=author)
book.save()

# Create a Library object
library = Library(name='Main')
library.save()

# Add the book to the library
library.books.add(book)

# Create a Librarian object
librarian = Librarian(name='Madam Pince', library=library)
librarian.save()

# Query all books in a specific library
library_name = 'Main'
library = Library.objects.get(name=library_name)
books = library.books.all()
print(f'Books in the {library_name} library:')
for book in books:
    print(book.title)

# Query all books by a specific author
author_name = 'J.K. Rowling'
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f'Books by {author_name}:')
for book in books_by_author:
    print(book.title)    

# Query all books in the library
books = library.books.all()
print('Books in the library:')
for book in books:
    print(book.title)

# Query the librarian of the library
librarian = Librarian.objects.get(library=library)
print(f'Librarian of the {library_name} library: {librarian.name}')

# Query the author of the book
author = book.author

print(f'Author of the book: {author.name}')

