# app_main/models.py

from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)