from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone



class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts",on_delete=models.CASCADE ,blank=True, null=True)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at', ]





