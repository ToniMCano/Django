

from django.contrib import admin
from django.urls import path , include
from . import views


urlpatterns = [
    
    path("" , views.home , name = 'home'),
    path('about/' , views.about , name = 'about'),
    path("services/" , include('services.urls')),
    path("blog/" , views.blog , name = 'blog'),
    path("tore" , views.store , name = 'store'),
    path("contact/" , views.contact , name = 'contact'),
    path("sample/" , views.sample , name = 'sample'),
    ]