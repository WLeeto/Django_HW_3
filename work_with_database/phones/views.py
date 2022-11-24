from django.http import HttpResponse
from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort is None:
        phone_obj = Phone.objects.all()
    elif sort == 'name':
        phone_obj = Phone.objects.all().order_by('name')
    elif sort == 'min_price':
        phone_obj = Phone.objects.all().order_by('price')
    elif sort == 'max_price':
        phone_obj = Phone.objects.all().order_by('-price')
    context = {
        'phones': phone_obj,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_obj = Phone.objects.get(slug=slug)
    context = {
        'phone': phone_obj,
    }
    return render(request, template, context)

