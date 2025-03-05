from django.shortcuts import render,redirect
from django.http import HttpRequest , HttpResponse
from .models import Blog

# Create your views here.
def home (request:HttpRequest):

    blogs = Blog.objects.all()

    return render(request,'main/index.html',{"blogs" : blogs})

def create(request:HttpRequest):

    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"], content=request.POST['content'],image=request.FILES['image'])
        new_blog.save()

        return redirect('main:home')

    return render(request , 'main/create.html')

def view(request:HttpRequest, blog_id):

    blog = Blog.objects.get(pk=blog_id)

    return render(request,'main/view.html',{"blog":blog})

def update(request:HttpRequest, blog_id):
    
    blog = Blog.objects.get(pk=blog_id)
    if request.method == "POST":
        blog.title = request.POST["title"]
        blog.content = request.POST["content"]
        if "image" in request.FILES:
            blog.image = request.FILES["image"]
        blog.save()

        return redirect('main:view',blog_id=blog.id)
    return render(request,'main/update.html',{"blog":blog})

def delete(request:HttpRequest, blog_id):
    
    blog = Blog.objects.get(pk=blog_id)
    blog.delete()

    return redirect("main:home")