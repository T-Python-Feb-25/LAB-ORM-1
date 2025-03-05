from django.shortcuts import render,redirect
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
        if not request.FILES.get("poster","")=="":
            t.update({"poster":request.FILES["poster"]})
        
        print(request.FILES)
        post=Post(**t)
        post.save()
        return redirect("main:home_view")

    return render(request,"main/post.html")
def detail_view(request:HttpRequest,id:int):
    post=Post.objects.get(pk=id)
    return render(request,"main/detail.html",{"post":post})
def update_view(request:HttpRequest,id:int):
    post=Post.objects.get(pk=id)
    if request.method=='POST':
        post.title=request.POST["title"]
        post.content=request.POST["content"]

        if not request.POST.get('is_published',"")=="":
            post.is_published=request.POST["is_published"]

        if not  request.POST.get('published_at',"")=="":
            post.published_at=request.POST["published_at"]
        if not request.FILES.get("poster","")=="":
            post.poster=request.FILES["poster"]
        post.save()

        return redirect("main:detail_view",id=post.id)
    return render(request,"main/update.html",{"post":post})
def delate_view(request:HttpRequest,id:int):
    post=Post.objects.get(pk=id)
    post.delete()
    return redirect("main:home_view")


