from django.db import models

# Create your models here.

class Services(models.Model):
    
    title = models.CharField( max_length = 50 , verbose_name = 'Título')
    subtitle = models.CharField( max_length = 50 , verbose_name = 'Subtítulo')
    content = models.TextField(verbose_name = "Contenido")
    image =  models.ImageField(upload_to = 'media/services' , verbose_name = 'Imagen')
    created = models.DateField(auto_now_add = True , verbose_name = "Fecha de Creación")
    updated = models.DateField(auto_now = True , verbose_name = "Fecha de Actualización")
    
    
    class Meta:
        
        verbose_name = 'Servicio'
        verbose_plurals = "Servicios"
        ordering = ['-created']
    
