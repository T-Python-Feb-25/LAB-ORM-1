from django.urls import path
from . import views


app_name="main"


urlpatterns=[
    path("" ,views.home_view ,name="home_view"),
    path("search/", views.search_blogs_view, name="search_blogs_view"),
    path("sort/<type>/", views.sort_blogs, name="sort_blogs"),


]