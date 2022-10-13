from django.contrib import admin
from django.urls import path, include
from card import views

#Переходы с главной страницы

from card.views import index
from card.views import base
from card.views import catalog

#Регистрация

from card.views import registerUser
from card.views import userLogin

#Магазин

from card.views import graphiccard
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

    #Категории магазина
    path('graphiccard.html/', graphiccard),
    path('cpu.html/', cpu),



]

