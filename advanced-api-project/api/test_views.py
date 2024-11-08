from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITests(APITestCase):
    """
        Setting up all the information I need like creating a user, author, book
        and creating the reverse URLs for create, detail, update, delete
    """
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass1234')
        self.author = Author.objects.create(name='Tuya')
        self.book = Book.objects.create(title='Test Book', publication_year=2020, author=self.author)
        self.create_url = reverse('book-create')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.update_url = reverse('book-update', kwargs={'pk': self.book.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book.pk})

    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpass1234')
        data = {'title': 'New Test Book', 'publication_year': 2022, 'author': self.author.pk}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Book.objects.get(pk=response.data['id']).title, 'New Test Book')

    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpass1234')
        update_data = {'title': 'Updated Test Book'}
        response = self.client.patch(self.update_url, update_data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Book.objects.get(pk=self.book.pk).title, 'Updated Test Book')

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpass1234')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, 204)

    def test_book_detail_view_permissions(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.login(username='testuser', password='testpass1234')
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
