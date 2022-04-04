from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Product, Category

# Create your views here.

def index(request): # pod odpytaniu wypluje cala zawartosc baz

    # jeden = Product.objects.filter(kategoria=1)
    category = Category.objects.all()
    dane = {'category' : category}
    return render(request, 'index.html', dane)

def category(request, id):
    category_user = Category.objects.get(pk=id)
    category_product = Category.objects.filters(category = category_user)
    category = Category.objects.all()
    dane = {'category_user' : category_user,
            'category_product' : category_product,
            'category' : category }
    return render(request, 'category_product.html', dane)

def product(request, id):
    product_user = Product.objects.get(pk=id)
    category = Category.objects.all()
    dane = {'product_user' : product_user, 'category' : category}

    return render(request, 'product.html', dane)