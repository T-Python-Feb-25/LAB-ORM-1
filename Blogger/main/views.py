from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
from .models import Blog

# Create your views here.
def home (request:HttpRequest):

    blogs = Blog.objects.all()

    return render(request,'main/index.html',{"blogs" : blogs})

def create(request:HttpRequest):

    if request.method == "POST":
        new_blog = Blog(title=request.POST["title"], content=request.POST['content'])
        new_blog.save()

    return render(request , 'main/create.html')