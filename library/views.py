from django.shortcuts import render, redirect, get_object_or_404
from .models import Book


def home(request):
    search = request.GET.get('search', '').strip()

    if search:
        books = Book.objects.filter(
            title__icontains=search
        ) | Book.objects.filter(
            author__icontains=search
        ) | Book.objects.filter(
            category__icontains=search
        )
    else:
        books = Book.objects.all()

    return render(request, 'home.html', {
        'books': books,
        'search': search
    })


def add_book(request):
    error = ''

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        author = request.POST.get('author', '').strip()
        category = request.POST.get('category', '').strip()
        isbn = request.POST.get('isbn', '').strip()
        available_copies = request.POST.get('available_copies', '').strip()

        if not title or not author or not category or not isbn or not available_copies:
            error = 'All fields are required.'

        elif not available_copies.isdigit():
            error = 'Available copies must be a number.'

        elif int(available_copies) < 0:
            error = 'Available copies cannot be negative.'

        elif Book.objects.filter(isbn=isbn).exists():
            error = 'This ISBN already exists.'

        else:
            Book.objects.create(
                title=title,
                author=author,
                category=category,
                isbn=isbn,
                available_copies=int(available_copies)
            )

            return redirect('/')

    return render(request, 'add_book.html', {'error': error})


def view_book(request, id):
    book = get_object_or_404(Book, id=id)

    return render(request, 'view_book.html', {
        'book': book
    })


def edit_book(request, id):
    book = get_object_or_404(Book, id=id)
    error = ''

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        author = request.POST.get('author', '').strip()
        category = request.POST.get('category', '').strip()
        isbn = request.POST.get('isbn', '').strip()
        available_copies = request.POST.get('available_copies', '').strip()

        if not title or not author or not category or not isbn or not available_copies:
            error = 'All fields are required.'

        elif not available_copies.isdigit():
            error = 'Available copies must be a number.'

        elif int(available_copies) < 0:
            error = 'Available copies cannot be negative.'

        elif Book.objects.filter(isbn=isbn).exclude(id=book.id).exists():
            error = 'This ISBN already exists.'

        else:
            book.title = title
            book.author = author
            book.category = category
            book.isbn = isbn
            book.available_copies = int(available_copies)

            book.save()

            return redirect('/')

    return render(request, 'edit_book.html', {
        'book': book,
        'error': error
    })


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)
    book.delete()

    return redirect('/')