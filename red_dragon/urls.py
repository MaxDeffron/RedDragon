from django.contrib import admin
from django.urls import path, include
from card import views


from card.views import catalog
from card.views import graphiccard
from card.views import login
from card.views import register

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('catalog.html/', catalog),
    path('graphiccard.html/', graphiccard),
    path('login.html/', login),
    path('login.html/sign-up.html/', register),
]

