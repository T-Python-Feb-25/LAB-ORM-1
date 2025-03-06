from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from blogs.models import Blog
def home_view(request:HttpRequest):

    #get all blogs
    blogs = Blog.objects.all()

    return render(request, 'main/index.html', {"blogs" : blogs} )
