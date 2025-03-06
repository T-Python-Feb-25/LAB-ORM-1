from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import post

# Create your views here.

def home(request:HttpRequest):
    #get all post
    posts=post.objects.all()
    return render(request, 'main/home.html/',{"posts":posts})


def new_post(request:HttpRequest):

    if request.method=="post":
        create_post=post(title=request.post["title"],content=request.post["content"],is_published=request.post["is_published"],published_at=request.post["published_at"])
        create_post.save()

    return render(request, 'main/new_posts.html/')
