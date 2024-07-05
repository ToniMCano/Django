from django.db import models

# Create your models here.

class Services(models.Model):
    
    title = models.CharField(max_length = 250 , verbose_name = "Título")
    subtitle = models.CharField(max_length = 250 , verbose_name = 'Subtítulo')
    image = models.ImageField(upload_to = 'services' , verbose_name = 'Imagen')
    content = models.TextField(verbose_name = "Contenido")
    created = models.DateField(auto_now_add = True , verbose_name = "Fecha de Creación")
    updated = models.DateField(auto_now = True , verbose_name = "Fecha de Actualización")
    
    
    class Meta:
        
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        
        ordering = ['-created']
        
        
    def __str__(self):
        
        return self.title