from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from post.models import Post
# Create your views here.
def home_view(request:HttpRequest):
  posts = Post.objects.all()
  return render(request, 'main/index.html', {"posts":posts})