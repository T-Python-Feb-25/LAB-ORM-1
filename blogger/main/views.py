from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm


def home(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    print(f"Number of posts fetched: {posts.count()}")  # Debugging
    return render(request, 'main/home.html', {'posts': posts})


def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'main/add_post.html', {'form': form})


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')