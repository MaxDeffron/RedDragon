from django.contrib import admin
from django.urls import path, include
from card import views

from card.views import catalog
from card.views import graphiccard
from card.views import login
from card.views import registerUser

from card.views import userLogin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('catalog.html/', catalog),
    path('graphiccard.html/', graphiccard),
    path('login.html/sign-up.html/', registerUser),
    path('login.html/', userLogin),
]

