from django.shortcuts import render , HttpResponse
from .models import Services

# Create your views here.

def services(request):
    
    all_services = Services.objects.all()
    
    return render(request , 'services/services.html' , {'services' : all_services})