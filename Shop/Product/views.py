from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.

def index(request): # pod odpytaniu wypluje cala zawartosc baz
    request_return = Product.objects.all()
    return HttpResponse(request_return)