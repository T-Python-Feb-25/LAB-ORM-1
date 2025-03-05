from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Post
# Create your views here.
def home_view(request:HttpRequest):
    post=Post.objects.all()
    
    
    return render(request,"main/home.html",{"post":post})
def post_view(request:HttpRequest):
    if request.method=='POST':
        t={"title":request.POST["title"],"content":request.POST["content"]}
        if not request.POST.get('is_published',"")=="":
            t.update({"is_published":request.POST["is_published"]})
        if not  request.POST.get('published_at',"")=="":
            t.update({"published_at":request.POST["published_at"]})
            
        post=Post(**t)
        post.save()
    
    return render(request,"main/post.html")