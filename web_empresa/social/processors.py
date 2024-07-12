from .models import Social

def social_elements(request):
    
    socials_dict = {}
    
    socials = Social.objects.all()
    
    for social in socials:
        
        socials_dict[social.key] = social.url
        
    return socials_dict
    
    
    