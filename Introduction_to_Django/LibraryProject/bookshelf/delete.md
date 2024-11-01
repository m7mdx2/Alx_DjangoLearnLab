# Delete Operation

# python command
book.delete()
all_books_after_delete = Book.objects.all()
print(all_books_after_delete)

# Expected Output: <QuerySet []>