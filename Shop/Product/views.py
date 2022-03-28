from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category

# Create your views here.

def index(request): # pod odpytaniu wypluje cala zawartosc baz
    # wszystkie = Product.objects.all()
    jeden = Product.objects.filter(kategoria=1)
    kat_name = Category.objects.get(id=2)
    kat_all = Category.objects.all()
    return HttpResponse(jeden)

def category(request, id):
    category_user = Category.objects.get(pk=id)
    return HttpResponse(category_user.nazwa)