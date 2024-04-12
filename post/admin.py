from django.contrib import admin
from .models import Post, Category, Comment

class CategoryAdmin(admin.ModelAdmin):
  list_display = ['title', 'slug', 'created_at']
  prepopulated_fields = {'slug': ('title',)}
  

class PostAdmin(admin.ModelAdmin):
  list_display = ['title', 'slug', 'updated_at', 'image_table']
  readonly_fields = ['image_table']
  list_filter = ['category']
  prepopulated_fields = {'slug': ('title',)}
  
class CommentAdmin(admin.ModelAdmin):
  list_display = ['name', 'status']
  list_filter = ['status']
  
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)