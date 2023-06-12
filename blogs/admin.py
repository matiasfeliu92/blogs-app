from django.contrib import admin
from .models import Category, Post
# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'category')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Post, PostsAdmin)
admin.site.register(Category, CategoryAdmin)