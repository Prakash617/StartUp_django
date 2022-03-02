from unicodedata import name
from django import views
from django.urls import path

from newsapp import views
urlpatterns = [
    path('', views.index, name='index'),
]