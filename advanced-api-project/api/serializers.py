from rest_framework import serializers
from .models import Book, Author
from datetime import date

# Serializer for the Book model, converting Book instances to and from JSON format.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_year', 'author']

    def validate_publication_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value
    # Ensures publication_year is not in the future.

# Serializer for the Author model, converting Author instances to and from JSON format.
# Uses BookSerializer to serialize related books dynamically.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']    