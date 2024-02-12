from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

def index(request):
    # Products = Product.objects.all()
    # Products = Products.object.filter()
    # Products = Products.object.get()
    # Products = Products.object.save()
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def new(request):
    return HttpResponse('New Product')