from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Blog

# Create your views here.

def create_blog_view(request:HttpRequest):

    
    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"], content = request.POST["content"], is_published=request.POST["is_published"],published_at=request.POST["published_at"])
        if "poster" in request.FILES: new_blog.poster = request.FILES["poster"]
        new_blog.save()

        return redirect('main:home_view')

    return render(request, "blogs/create.html")


def blog_detail_view(request:HttpRequest, blog_id:int):

    blog = Blog.objects.get(pk=blog_id)

    return render(request, 'blogs/blog_detail.html', {"blog" : blog})


def blog_update_view(request:HttpRequest, blog_id:int):

    blog = Blog.objects.get(pk=blog_id)

    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        blog.published_at = request.POST["published_at"]
        blog.is_published = request.POST["is_published"]
        if "poster" in request.FILES: blog.poster = request.FILES["poster"]
        blog.save()



        return redirect("blogs:blog_detail_view", blog_id=blog.id)

    return render(request, "blogs/blog_update.html", {"blog":blog})


def blog_delete_view(request:HttpRequest, blog_id:int):

    blog = Blog.objects.get(pk=blog_id)
    blog.delete()

    return redirect("main:home_view")