from django.db import models

# Create your models here.
'''title : char field (max 2048)
content : text field.
is_published : boolean field, default is True.
published_at : datetime field, default is now.'''

class post(models.Model):
    title=models.CharField(max_length=2048)
    content=models.TextField()
    is_published=models.BooleanField(default=True)
    published_at=models.DateTimeField(auto_now=True)

