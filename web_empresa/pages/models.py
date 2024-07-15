from django.db import models



class Page(models.Model):
    
    title = models.CharField(verbose_name = "Título", max_length=50)
    content = models.TextField(verbose_name = "Contenido")
    created = models.DateField(auto_now_add = True , verbose_name = 'Fecha de Creación')
    updated = models.DateField(auto_now = True , verbose_name = 'Fecha de Actualización')
    
    class Meta:
        
        verbose_name = "página"
        verbose_name_plural = "páginas"
        
        ordering = ["title"]
        
    def __str__(self):
        
        return self.title