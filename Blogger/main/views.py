from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from blogs.models import Blog
def home_view(request:HttpRequest):
    if "sort" in request.COOKIES:
        sort_type = request.COOKIES['sort'] 
    if sort_type == "dec":
        blogs = Blog.objects.all().order_by('-published_at')
    elif sort_type == "inc":
        blogs = Blog.objects.all().order_by('published_at')
    else:
        blogs = Blog.objects.all() 

    return render(request, 'main/index.html', {"blogs": blogs})

def search_blogs_view(request:HttpRequest):
    if "search" in request.GET:
        blogs = Blog.objects.filter(title__contains=request.GET["search"])
    else:
        blogs=[]

    return render(request, 'main/index.html', {"blogs" : blogs}  )

def sort_blogs(request: HttpRequest,type: str) :

    response = redirect(request.GET.get("next", "/"))
    response.set_cookie("sort", type)
    return response


