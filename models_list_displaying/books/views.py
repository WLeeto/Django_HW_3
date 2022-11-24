from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books,
    }
    return render(request, template, context)


def books_pagi(request, pub_date):
    template = 'books/books_list_pagi.html'
    date_list = [date.pub_date for date in Book.objects.all()]
    print(date_list)
    book = Book.objects.all().get(pub_date=pub_date)

    page_number = pub_date
    paginator = Paginator(date_list, 1)
    page = paginator.get_page(page_number)
    context = {
        'books': book,
        'page': page,
    }
    return render(request, template, context)

