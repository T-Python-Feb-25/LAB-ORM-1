from django.shortcuts import render, redirect
from .models import Post


def add_post(request):
    if request.method == 'POST':

        new_post = Post(title = request.POST.get('title'), content = request.POST.get('content'), published_at = request.POST.get('published_at'), is_published = request.POST.get('is_published') == 'on',image=request.FILES["image"])
        new_post.save()
        return redirect('app_main:home')
    return render(request, 'app_main/add_post.html')

def home(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'app_main/home.html', {'posts': posts})