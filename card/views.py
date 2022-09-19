from django.shortcuts import render

from .models import Product

def index (request):
    return render(request, "index.html")

def catalog (request):
    return render(request, "catalog.html")

def graphiccard (request):
    product = Product.objects.all()
    videomemory = Product.objects.all()
    frequency = Product.objects.all()
    power = Product.objects.all()
    image = Product.objects.all()
    return render(request, "graphiccard.html", {'product':product, 'videomemory':videomemory, 'frequency':frequency, 'power':power, 'image':image})