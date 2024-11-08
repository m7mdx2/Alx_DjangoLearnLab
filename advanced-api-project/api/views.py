from django.shortcuts import render
from rest_framework import generics, status, filters
from .models import Book
from .serializers import BookSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated 
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as django_filters

# List all books or create a new one
class BookListView(generics.ListCreateAPIView):
    
    # Retrieve a list of all books or create a new book.
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly] # Public access for list, authenticated for create

    # Add filtering, searching, and ordering capabilities
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    # Specify which fields the user can filter by
    filterset_fields = ['title', 'author', 'publication_year']
    # Specify which fields can be searched using the SearchFilter
    search_fields = ['title', 'author']
    # Specify fields that can be ordered by
    ordering_fields = ['title', 'publication_year']
    # Specify the default ordering if no specific order is requested
    ordering = ['title']

    def post(self, request, *args, **kwargs):
         
        # Handle the creation of a new book with custom validation.
        
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    
    # Retrieve, update, or delete a book by its ID.
    
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Authenticated for update/delete, public for read

    def put(self, request, *args, **kwargs):
        
        # Handle the update of an existing book.
        
        return super().put(request, *args, **kwargs)

# Create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can create


# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can update


# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete