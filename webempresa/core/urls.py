from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home , name = "index"),
    path('historia/', views.about , name = "about"),
    path('store/', views.store , name = "store"),
    path('visitanos/', views.visit_us , name = "visit_us"),
    path('blog/', views.blog , name = "blog"),
    path('sample/', views.sample , name = "sample"),
    path('contacto/', views.contact , name = "contact"),

]

