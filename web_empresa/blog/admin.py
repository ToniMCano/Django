from django.contrib import admin
from .models import Categories , Post

# Register your models here.

class CategoriesAdmin(admin.ModelAdmin):
    
    readonly_fields = ('created' , 'updated')
    
    
class PostAdmin(admin.ModelAdmin):
    
    readonly_fields = ('created' , 'updated')
    list_display = ('title' , 'author' , 'published' , 'post_categories')
    ordering = ('author',)
    search_fields = ('title' , 'author__username' , 'content' , 'categories__title')
    date_hierarchy = 'published'
    list_filter = ('author__username' , 'categories__title')
    
    def post_categories(self , obj):

        return ", ".join([ c.title for c in obj.categories.all()])
    
    post_categories.short_description = 'Categorías'
    
admin.site.register(Categories  , CategoriesAdmin)
admin.site.register(Post , PostAdmin)