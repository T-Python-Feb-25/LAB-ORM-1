from django.db import models

# Create your models here.


class blogger(models.Model):
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)
    poster = models.ImageField(upload_to='images/', default="images/default.jpg", blank=True)
    
    