from django.shortcuts import render

from .models import Product
from django.contrib.auth.forms import UserCreationForm

def index (request):
    return render(request, "index.html")

def catalog (request):
    return render(request, "catalog.html")

def login (request):
    return render(request, "../templates/registration/login.html")

def register (request):
    form = UserCreationForm()
    return render(request, "../templates/registration/sign-up.html", {"form": form})

def graphiccard (request):
    product = Product.objects.all()
    videomemory = Product.objects.all()
    frequency = Product.objects.all()
    power = Product.objects.all()
    image = Product.objects.all()
    return render(request, "graphiccard.html", {'product':product, 'videomemory':videomemory, 'frequency':frequency, 'power':power, 'image':image})