from django.contrib import admin
from django.contrib.auth.models import User

from .models import Post

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    list_display = [id,'user' , 'text']