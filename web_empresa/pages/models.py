from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

class Page(models.Model):
    
    title = models.CharField(max_length = 250 , verbose_name = "Título")
    content = CKEditor5Field('Text', config_name='extends' , default = "1")
    order = models.SmallIntegerField(verbose_name = "Orden" , default = 0)
    created = models.DateField(auto_now_add = True)
    updated = models.DateField(auto_now = True)
    
    
    class Meta:
        
        verbose_name = "página"
        verbose_name_plural = "páginas"
        
        ordering = ['order' , 'title']
        
    def __str__(self):
        
        return self.title
    
    
    