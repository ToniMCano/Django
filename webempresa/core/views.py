from django.shortcuts import render

# Create your views here.

def home(request):
    
    return render(request , 'core/index.html')


def about(request):
    
    return render(request , 'core/historia.html')


def services(request):
    
    return render(request , 'core/servicios.html')


def store(request):
    
    return render(request , 'core/store.html')


def visit_us(request):
    
    return render(request , 'core/visitanos.html')


def blog(request):
    
    return render(request , 'core/blog.html')


def contact(request):
    
    return render(request , 'core/contacto.html')


def sample(request):
    
    return render(request , 'core/sample.html')

