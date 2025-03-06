from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Post
# Create your views here.

def Home_view(request: HttpRequest):
    posts=Post.objects.all()
    return render(request, "main/index.html",{"posts":posts})

def Creat_post_view(request: HttpRequest):
    if request.method=="POST":
        new_post=Post(title=request.POST["title"],content=request.POST["content"],is_published=request.POST["is_published"],published_at=request.POST["published_at"] )
        new_post.save()
    return render(request, "main\creat_post.html")