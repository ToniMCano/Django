from django.shortcuts import render , redirect
from  .forms import ContactForm
from django.urls import reverse
from django.core.mail import EmailMessage

# Create your views here.

def contact(request):
    
    form = ContactForm()
    
    if request.method == 'POST':
        form = ContactForm(data = request.POST)
        
        if form.is_valid():
            name = request.POST.get("name" , "")
            email = request.POST.get("email" , "")
            content = request.POST.get("content" , "")
            
            email_to = EmailMessage(
                "Asunto del Mail",
                f"{name} , {email} , \n\n {content}",
                'provwork2015@gmail.com',
                ['provwork2015@gmail.com'],
                reply_to = ['provwork2015@gmail.com'] 
            )
            
            try:
                email_to.send()
            except Exception as e:
                print('no ha funcionado' , e)

                return redirect(reverse('contact') + '?fail')
           
    
    return render(request , 'contact/contact.html' , {'form' : form})