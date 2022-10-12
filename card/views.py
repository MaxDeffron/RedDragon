from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import registerUserForm, userLoginForm
from django.contrib.auth import login, logout

def index (request):
    return render(request, "index.html")

def catalog (request):
    return render(request, "catalog.html")

def registerUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect("../templates/registration/login.html")
        else:
            messages.error(request, 'Error registration')
    else:
        form = registerUserForm()
    return render(request, "../templates/registration/sign-up.html", {"form": form})

def userLogin(request):
    if request.method == 'POST':
        form = userLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            redirect("../templates/registration/login.html")
    else:
        form =userLoginForm()
    return render(request, "../templates/registration/login.html", {"form": form})

def graphiccard (request):
    product = Product.objects.all()
    videomemory = Product.objects.all()
    frequency = Product.objects.all()
    power = Product.objects.all()
    image = Product.objects.all()
    return render(request, "graphiccard.html", {'product':product, 'videomemory':videomemory, 'frequency':frequency, 'power':power, 'image':image})