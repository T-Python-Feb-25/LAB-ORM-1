from django.shortcuts import render, redirect

# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template.defaultfilters import title

# Create your views here.
from .models import Post

def main_view(request: HttpRequest):
    #get all posts
    posts = Post.objects.all()

    return render(request, "main/mainpage.html", {"posts": posts})

def post_view(request: HttpRequest):
    if request.method == "POST":
        new_post = Post(title=request.POST['title'], content=request.POST['content'], published_at=request.POST['published_at'],is_published=request.POST['is_published'],image=request.FILES['image'])
        new_post.save()
        return redirect('main:main_view')
    return render(request, "main/postpage.html")

def post_detail_view(request: HttpRequest, post_id:int):
    post = Post.objects.get(pk=post_id)
    return render(request, "main/post_detail.html", {"post": post})

def post_update_view(request: HttpRequest, post_id:int):
    post = Post.objects.get(pk=post_id)
    if request.method == "POST":
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.published_at = request.POST['published_at']
        post.is_published = request.POST['is_published']
        if 'image' in request.FILES:
            post.image = request.FILES['image']


        post.save()
        return redirect('main:post_detail_view',post_id=post_id)

    return render(request, "main/post_update.html", {"post": post})


def post_delete_view(request: HttpRequest, post_id: int):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('main:main_view')
