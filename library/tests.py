from django.test import TestCase
from django.urls import reverse

from .models import Book


class BookTestCase(TestCase):

    def setUp(self):
        self.book = Book.objects.create(
            title='Python Programming',
            author='John Smith',
            category='Programming',
            isbn='TEST-ISBN-001',
            available_copies=5
        )

    def test_book_created(self):
        self.assertEqual(Book.objects.count(), 1)

    def test_home_page(self):
        response = self.client.get(reverse('home'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Python Programming')

    def test_view_book(self):
        response = self.client.get(
            reverse('view_book', args=[self.book.id])
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Python Programming')

    def test_edit_book(self):
        response = self.client.post(
            reverse('edit_book', args=[self.book.id]),
            {
                'title': 'Python Programming Basics',
                'author': 'John Smith',
                'category': 'Programming',
                'isbn': 'TEST-ISBN-001',
                'available_copies': '10'
            }
        )

        self.assertEqual(response.status_code, 302)

        self.book.refresh_from_db()

        self.assertEqual(
            self.book.title,
            'Python Programming Basics'
        )

        self.assertEqual(
            self.book.available_copies,
            10
        )

    def test_delete_book(self):
        response = self.client.get(
            reverse('delete_book', args=[self.book.id])
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.count(), 0)