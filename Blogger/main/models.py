from django.db import models
from django.utils import timezone
def now_no_microseconds():
    current_time = timezone.now()
    return current_time.replace(microsecond=0)
class Post(models.Model):
    title  = models.CharField(max_length=2048)
    content  = models.TextField()
    is_published  = models.BooleanField(default=True)
    published_at=models.DateTimeField(default=now_no_microseconds)
    poster = models.ImageField(upload_to="images/",default="images/d.jpeg")

