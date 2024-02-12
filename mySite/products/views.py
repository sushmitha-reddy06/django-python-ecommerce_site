from django.http import HttpResponse
from django.shortcuts import render
from .models import Vegetable, Fruit


def index(request):
    vegetables = Vegetable.objects.all()
    return render(request, 'index.html', {'vegetables': vegetables})


def fruits(request):
    fruits = Fruit.objects.all()
    return render(request, 'fruits.html', {"fruits": fruits})


def contact(request):
    return render(request, 'contact.html')
