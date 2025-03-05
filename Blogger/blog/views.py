from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Post
from .forms import PostForm
from django.contrib import messages

# View to display the latest posts
def home(request):
    posts = Post.objects.filter(is_published=True).order_by('-published_at')
    return render(request, 'blog/home.html', {'posts': posts})

# View to add a new post
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'blog/add_post.html', {'form': form})

# View to delete a post
def delete_post(request, post_id):
    # Get the post to delete or 404 if it doesn't exist
    post = get_object_or_404(Post, id=post_id)
    
    # If the user is authenticated (optional - you can check for permissions here)
    if post:
        post.delete()  # Delete the post from the database
    # Add a success message
        messages.success(request, 'The post has been deleted successfully.')
    # Redirect to the homepage after deletion
    return redirect('home')

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})

def unpublished_blogs(request):
    unpublished_posts = Post.objects.filter(is_published=False)
    return render(request, 'blog/unpublished_blogs.html', {'posts': unpublished_posts})

def publish_post(request, post_id):
    # Get the post by ID
    post = Post.objects.get(id=post_id)

    # Set is_published to True
    post.is_published = True
    post.save()

    # Add a success message to be shown to the user
    messages.success(request, 'Blog has been published successfully!')

    # Redirect to the unpublished blogs page after publishing
    return redirect('unpublished_blogs')  # This will redirect to the correct URL pattern for unpublished blogs