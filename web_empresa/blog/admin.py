from django.contrib import admin
from . models import Category , Post

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    
    readonly_fields = ('created' , 'updated')
    
admin.site.register(Category , CategoryAdmin)


class PostAdmin(admin.ModelAdmin):
    
    readonly_fields = ('created' , 'updated')
    list_display = ('title' , 'author' , 'published' , 'post_categories')
    search_fields = ('title' , 'author__username' , 'content' , 'categories__name')
    date_hierarchy = 'published'
    list_filter = ('author__username' , 'categories__name')
    
    
    def post_categories(self , obj):
        
        return '.'.join([c.name for c in obj.categories.all()])
    
    
    post_categories.short_description = 'Categorías'

    
    
admin.site.register(Post , PostAdmin)