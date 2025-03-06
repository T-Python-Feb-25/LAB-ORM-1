from django.shortcuts import render, redirect, get_object_or_404
from posts.models import Post
from django.utils import timezone
from django.http import HttpRequest
from posts.forms import PostForm  

def home(request):
    posts = Post.objects.filter(is_published=True)

    #Filter posts by specific date
    days_ago = timezone.now() - timezone.timedelta(days=3)
    posts = posts.filter(published_at__gte= days_ago)

    # Exclude posts
    posts = posts.exclude(title__icontains="Benefits ")

    # # Sort posts from newest to oldest
    posts = posts.order_by('-published_at')

    return render(request, 'blog/home.html', {'posts': posts})

def new_post(request):
    if request.method == "POST":
        title = request.POST["title"]
        content = request.POST["content"]
        image = request.FILES.get("image")  
        Post.objects.create(
            title=title,
            content=content,
            image=image,
            published_at=timezone.now()
        )
        return redirect('home')
    return render(request, 'blog/new_post.html')

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'post': post})

def post_delete(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect('home')
    return render(request, 'blog/post_delete.html', {'post': post})

def mode_view(request: HttpRequest, mode):
    response = redirect(request.GET.get("next", "/"))
    if mode in ["light", "dark"]:
        response.set_cookie("mode", mode, max_age=60*60*24*30)  
    return response

def contact(request):
    return render(request, 'blog/contact.html')