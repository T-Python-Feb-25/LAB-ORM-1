from django.shortcuts import render, redirect
from .models import blogger
from django.utils import timezone

# Create your views here.


def home(request):
    posts = blogger.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'homepage.html', {'posts': posts})

def posts(request):
    if request.method == 'POST':
     new_post = blogger(title=request.POST['title'], content=request.POST['content'], published_at=timezone.now(), poster=request.FILES['poster'])
     new_post.save()
     return redirect('home')
    return render(request, 'posts.html')

def detail(request, post_id:int):
    post = blogger.objects.get(pk=post_id)
    return render (request, 'detail.html', {'post': post})

def update (request, post_id:int):
    post = blogger.objects.get(pk=post_id)
    if request.method == 'POST':
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.published_at = timezone.now()
        if 'poster' in request.FILES:
            post.poster = request.FILES['poster']
            post.save()
        post.save()
        
        return redirect('main:detail', post_id=post.id)
    return render (request, 'update.html', {'post': post})

def delete(request, post_id:int):
    post = blogger.objects.get(pk=post_id)
    post.delete()
    return redirect('main:home')