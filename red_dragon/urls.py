from django.contrib import admin
from django.urls import path, include


from card import views


from card.views import *

#Переходы с главной страницы

from card.views import index
from card.views import base
from card.views import catalog

#Регистрация

from card.views import registerUser
from card.views import userLogin

#Магазин

from card.views import graphiccard
from card.views import ManufacturerList
from card.views import cpu



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),

    #Переход с главной страницы
    path('index.html/', index), #на главную страницу
    path('base.html/', base),
    path('login.html/', userLogin),
    path('login.html/sign-up.html/', registerUser),
    path('catalog.html/', catalog),

    #Шаблоны регистрации/входа
    path('login.html/sign-up.html/', registerUser),
    path('login.html/', userLogin),
    path('orders.html/', ordersUser),


    #Категории магазина
    path('manufacturer_list.html/', graphiccard),
   #path('manufacturer_list.html/', ManufacturerList.as_view()),
    path('manufacturer_list.html/', views.ManufacturerListFilter.as_view(), name='filter'),
    path('cpu.html/', cpu),
]

