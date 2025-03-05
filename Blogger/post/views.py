from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.
from .models import Post
from django.contrib import messages

def create_view(request:HttpRequest):

  #messages.success(request, "Sent successfully!")
  if request.method == "POST":
    new_post=Post(
       title=request.POST["title"], 
       content=request.POST["content"], 
       is_published=request.POST["is_published"],
       published_at=request.POST["published_at"],
       poster=request.FILES['poster'])
    new_post.save()
    return redirect("main:home_view")


  return render(request, "post/create.html")
  
def post_detail_view(request:HttpRequest, post_id:int):
  post = Post.objects.get(pk=post_id)
  return render(request, "post/detail.html", {"post": post})

def post_update_view(request:HttpRequest, post_id:int):
  post = Post.objects.get(pk=post_id)
  if request.method == "POST":
    post.title = request.POST["title"]
    post.content = request.POST["content"]
    post.is_published = request.POST["is_published"]
    post.published_at = request.POST["published_at"]
    if "poster" in request.FILES:
       post.poster = request.FILES['poster']
    post.save()
    return redirect("post:post_detail_view", post_id=post.id)
  return render(request, 'post/update.html', {'post':post})

def post_delete_view(request:HttpRequest, post_id:int):
  post = Post.objects.get(pk=post_id)
  post.delete()

  return redirect("main:home_view")
