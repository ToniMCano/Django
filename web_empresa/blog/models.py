from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Categories(models.Model):
    
    title = models.CharField(max_length = 250 , verbose_name = 'Nombre') 
    created = models.DateField(auto_now_add = True , verbose_name = 'Fecha de Creación') 
    updated = models.DateField(auto_now = True , verbose_name = 'Fecha de Actualización') 
    
        
    class Meta:
        
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        
        ordering = ['-created']
        
    
    def __str__(self):
        
        return self.title
    

class Post(models.Model):
    
    title = models.CharField(max_length=250 , verbose_name = 'Título')
    content = models.TextField(verbose_name = 'Contenido')
    published = models.DateTimeField(verbose_name = 'Fecha de Creación' , default = now) 
    image = models.ImageField(blank = True , null = True , verbose_name = 'Imagen' , upload_to = 'blog')
    author = models.ForeignKey(User , verbose_name = 'Autor' , on_delete = models.CASCADE)
    categories = models.ManyToManyField(Categories , verbose_name = 'Categorías' , related_name = "get_post")
    created = models.DateField(auto_now_add = True , verbose_name = 'Fecha de Creación') 
    updated = models.DateField(auto_now = True , verbose_name = 'Fecha de Actualización') 
    
        
    class Meta:
        
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        
        ordering = ['-created']
        
    
    def __str__(self):
        
        return self.title
