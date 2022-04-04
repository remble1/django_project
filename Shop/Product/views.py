from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Product, Category

# Create your views here.

def index(request): # pod odpytaniu wypluje cala zawartosc baz

    # jeden = Product.objects.filter(kategoria=1)
    category = Category.objects.all()
    dane = {'category' : category}
    return render(request, 'szablon.html', dane)

def category(request, id):
    category_user = Category.objects.get(pk=id)
    return HttpResponse(category_user.nazwa)

def product(request, id):
    product_user = Product.objects.get(pk=id)
    sample = '<h1>' + str(product_user) + '</h1>' + \
             '<p>' + str(product_user.opis) + '<p>' + \
             '<p>' + str(product_user.cena) + '<p>'
    # to tylko test, tak nie można robić
    return HttpResponse(sample)