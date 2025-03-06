from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=2048)
    content = models.TextField()
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title