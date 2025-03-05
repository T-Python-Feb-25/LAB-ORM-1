from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=2048)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    published_at = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images/',default="images/default.png" ,null=True, blank=True)

    def __str__(self):
        return self.title
