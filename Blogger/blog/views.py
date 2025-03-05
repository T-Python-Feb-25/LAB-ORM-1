#from django.shortcuts import render

from django.shortcuts import render, redirect
from .models import Post
from django.utils import timezone

def homepage(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'blog/home.html', {'posts': posts})

def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        is_published = request.POST.get('is_published', 'on') == 'on'
        post = Post(title=title, content=content, is_published=is_published, published_at=timezone.now())
        post.save()
        return redirect('homepage')
    
    return render(request, 'blog/add_post.html')
