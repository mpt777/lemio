from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'file')

admin.site.register(Post, PostAdmin)
