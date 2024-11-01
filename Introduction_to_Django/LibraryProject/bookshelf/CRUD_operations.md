# Create Operation

# python command
book = Book(title="1984", author="George Orwell", publication_year=1949)
book.save()

# Expected Output: A confirmation message if saved successfully

# Retrieve Operation

# python command
all_books = Book.objects.all()
print(all_books)

# Expected output = <QuerySet [<Book: 1984>]>

# Update Operation

# python command
book.title = "Nineteen Eighty-Four"
book.save()

# Expected Output: A confirmation message if updated successfully

# Delete Operation

# python command
book.delete()
all_books_after_delete = Book.objects.all()
print(all_books_after_delete)

# Expected Output: <QuerySet []>