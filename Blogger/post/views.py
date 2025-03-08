from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
# Create your views here.
from .models import Post
from django.contrib import messages
from .forms import PostForm
def create_view(request:HttpRequest):
  post_form = PostForm()

  #messages.success(request, "Sent successfully!")
  if request.method == "POST":
    post_form = PostForm(request.POST, request.FILES)
    if post_form.is_valid():
      post_form.save()
      return redirect('main:home_view')
    else:
      print("not found")
    #new_post=Post(
    #   title=request.POST["title"], 
    #   content=request.POST["content"], 
    #   is_published=request.POST["is_published"],
    #   published_at=request.POST["published_at"],
    #   poster=request.FILES['poster'])
    #new_post.save()
    #return redirect("main:home_view")


  return render(request, "post/create.html", {"post_form": post_form})
  
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

def all_post_view(request:HttpRequest):
   post= Post.objects.all().order_by("-published_at")
   return render(request, "post/all_post.html", {"post":post})

def search_post_view(request: HttpRequest):
  if "Search" in request.GET and len(request.GET["Search"]) >=3:
    post = Post.objects.filter(title__contains=request.GET["Search"])

    if "order_by" in request.GET and request.GET["order_by"] == "is_published":
        post= post.order_by("-is_published")
    elif "order_by" in request.GET and request.GET["order_by"] == "published_at":
         post = post.order_by("-published_at")

  else:
    post = []
  return render(request, "post/search_post.html", {"post":post})