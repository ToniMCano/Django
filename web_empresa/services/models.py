from django.db import models

# Create your models here.

class Services(models.Model):
    
    title = models.CharField(max_length = 200 , verbose_name = "Título")
    subtitle = models.CharField(max_length = 200 , verbose_name = "Subtítulo")
    content =  models.TextField(verbose_name = "Contenido")
    image =  models.ImageField(upload_to = 'services')
    created = models.DateField(auto_now_add = True) # Establece la fecha de creación automáticamente
    updated = models.DateField(auto_now = True) # Buscar la diferencia entre este y auto_now_add.
    
    class Meta:
        
        verbose_name = "Servicio"
        verbose_name_plural = "Servicios"
        
        ordering = ['-created']
        
    def __str__(self):
        
        return self.title