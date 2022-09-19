from django.contrib import admin
from django.urls import path, include
from card import views


from card.views import catalog
from card.views import graphiccard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('catalog.html/', catalog),
    path('graphiccard.html/', graphiccard),
]
