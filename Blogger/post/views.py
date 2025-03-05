from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
# Create your views here.
from .models import Post
from django.contrib import messages

def create_view(request:HttpRequest):

  messages.success(request, "Sent successfully!")
  if request.method == "POST":
    new_post=Post(
       title=request.POST["title"], 
       content=request.POST["content"], 
       is_published=request.POST["is_published"],
       published_at=request.POST["published_at"])
    new_post.save()

  return render(request, "post/create.html")
  
