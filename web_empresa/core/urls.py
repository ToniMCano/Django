from django.contrib import admin
from django.urls import path , include
from . import views
from django.conf import settings

urlpatterns = [
    path("" , views.home , name = "home"),
    path("about/" , views.about , name = "about"),
    path("blog/" , views.blog , name = "blog"),
    path("store/" , views.store , name = "store"),
    path("contact/" , views.contact , name = "contact"),
    path("sample/" , views.sample , name = "sample"),
]


if settings.DEBUG:
    
    from django.conf.urls.static import static
    
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)