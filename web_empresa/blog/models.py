from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    
    name = models.CharField(max_length = 200 , verbose_name = 'Nombre')
    
    created = models.DateField(auto_now_add = True , verbose_name = 'Fecha de Creación')
    updated = models.DateField(auto_now = True)
    
    
    class Meta:
        
        verbose_name = "categoría"
        verbose_name_plural = 'categorías'
        
        ordering = ['name']
    
    def __str__(self):
        
        return self.name
    
    
class Post(models.Model):
    
    title = models.CharField(max_length = 250 , verbose_name = 'Título')
    content = models.TextField(verbose_name = "Contenido")
    author = models.ForeignKey(User , verbose_name = "Autor" , on_delete = models.CASCADE)
    published = models.DateTimeField(verbose_name = "Fecha de Publicación" , default = now)
    image = models.ImageField(verbose_name = "Imagen" , upload_to = 'blog' , blank = True , null = True)
    categories = models.ManyToManyField(Category , verbose_name = "Categorías" , related_name = "get_posts") 
    
    created = models.DateField(auto_now_add = True , verbose_name = "Fecha de Creación")
    updated = models.DateField(auto_now = True , verbose_name = "Fecha de Actualización")
    
    
    class Meta:
        
        verbose_name = "post"
        verbose_name_plural = 'posts'
        
        ordering = ['-created']


    def __str__(self):
        
        return self.title