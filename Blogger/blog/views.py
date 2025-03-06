#from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone
from django.http import HttpRequest, HttpResponse

def homepage(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'blog/home.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        is_published = request.POST.get('is_published', 'on') == 'on'
        post = Post(title=title, content=content, is_published=is_published, published_at=timezone.now(),poster=request.FILES["poster"])
        post.save()
        return redirect('blog:homepage')
    
    return render(request, 'blog/add_post.html')



def details(request:HttpRequest, blog_id:int):

    post = Post.objects.get(pk=blog_id)

    return render(request, 'blog/details.html', {"post" : post})