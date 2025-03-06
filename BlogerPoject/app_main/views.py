

from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def post_details_and_edit(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "POST":
        if 'delete' in request.POST:
            post.delete()
            return redirect('home')
        
      
        post.title = request.POST["title"]
        post.content = request.POST["content"]
        post.is_published = request.POST.get("is_published") == "yes"
        if request.FILES.get("image"):
            post.image = request.FILES["image"]
        post.save()
        return redirect('post_details', post_id=post.id)

    return render(request, "app_main/post_details_edit.html", {"post": post})