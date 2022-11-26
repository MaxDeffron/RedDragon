import json

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import registerUserForm, userLoginForm
from django.contrib.auth import login, logout
from .filters import ClientFilter
from .filters import SearchClientFilter
from django.contrib.auth.decorators import login_required

from django.http import JsonResponse
import json



# Импорт моделей БД

from .models import Product
from .models import Manufacturer
from .models import Cart
from .models import CartItem

# Импорт ListView

from django.views.generic import ListView


# Переходы с главной страницы

def index (request):
    return render(request, "index.html")

def catalog (request):
    return render(request, "catalog.html")

def base (request):
    return render(request, "../templates/base/base.html")

@login_required(login_url= '/login.html')
def ordersUser (request):
    return render(request, "orders.html")

@login_required(login_url= '/login.html')
def profileUser (request):
    return render(request, "profile.html")

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
                                                                        'id': id,

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
            user = form.save()
            login(request, user)
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
            return redirect("/profile.html")
    else:
        form =userLoginForm()
    return render(request, "../templates/registration/login.html", {"form": form})

def userLogout(request):
    logout(request)
    return redirect("../templates/registration/login.html")

#Корзина

def cart(request):

    cart = None
    cartitems = []

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitems = cart.cartitems.all()




    context = {"cart":cart, "items":cartitems}
    return render(request, "../templates/cart/cart.html", context)

def addToCart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Product.objects.get(id=product_id)
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created = CartItem.objects.get_or_create(cart=cart, product=product)
        cartitem.quantity += 1
        cartitem.save()
        print(cartitem)

    return JsonResponse("It is working", safe=False)





    #data = json.load(request.body)
    #item_id = data["id"]
    #product = Product.objects.get(id=item_id)

    #if request.user.is_authenticated:
    #    cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
    #return JsonResponse("It is working", safe=False)

