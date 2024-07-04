
from django.urls import path , include
from . import views


urlpatterns = [
    
    path("" , views.home , name = 'home'),
    path('about/' , views.about , name = 'about'),
    path("services/" , include('services.urls')),
    path("store" , views.store , name = 'store'),
    path("blog/" , include('blog.urls')),
    path("contact/" , views.contact , name = 'contact'),
    path("sample/" , views.sample , name = 'sample'),
    ]