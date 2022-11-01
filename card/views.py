from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import registerUserForm, userLoginForm, productSelect
from django.contrib.auth import login, logout
from django.views.generic.base import View
from django_filters.rest_framework import DjangoFilterBackend
from  django_filters import rest_framework as filters
from .filters import ClientFilter
from .filters import SearchClientFilter
from rest_framework.filters import SearchFilter, OrderingFilter


# Импорт моделей БД

from .models import Product
from .models import Manufacturer

# Импорт ListView

from django.views.generic import ListView


# Переходы с главной страницы

def index (request):
    return render(request, "index.html")

def catalog (request):
    return render(request, "catalog.html")

def base (request):
    return render(request, "../templates/base/base.html")

def ordersUser (request):
    return render(request, "orders.html")

# Шаблоны интернет магазина



def graphiccard (request):
    product = Product.objects.all()
    clientFilter = ClientFilter(request.GET, queryset=product,)
    product = clientFilter.qs

    searchClientFilter = SearchClientFilter(request.GET, queryset=product,)
    product = searchClientFilter.qs

    videomemory = Product.objects.all()
    frequency = Product.objects.all()
    power = Product.objects.all()
    image = Product.objects.all()


    #if request.method == 'POST':
       # pass
   # else:
     #   form = productSelect
    return render(request, "../templates/card/manufacturer_list.html", {'product': product,
                                                                        'videomemory': videomemory,
                                                                        'frequency': frequency,
                                                                        'power': power,
                                                                        'image': image,
                                                                        'clientFilter':clientFilter,
                                                                        'searchClientFilter': searchClientFilter,

                                                                        #'form':form,
                                                                  })



class ManufacturerList(ListView):
    model = Manufacturer

    def get_name(self):
        return Manufacturer.objects.all()



class ManufacturerListFilter(ManufacturerList, ListView):
    def get_queryset(self):
        queryset = Manufacturer.objects.filter(name__in=self.request.GET.getlist("name"))
        return queryset



def cpu (request):
    return render(request, "../templates/shop/cpu.html")

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
    return render(request, "../templates/profile.html", {"form": form})






