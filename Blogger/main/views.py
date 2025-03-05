from django.shortcuts import render

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
        new_post = Post(title=request.POST['title'], content=request.POST['content'], published_at=request.POST['published_at'],is_published=request.POST['is_published'])
        new_post.save()

    return render(request, "main/postpage.html")