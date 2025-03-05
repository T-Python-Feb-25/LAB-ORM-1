from django.urls import path
from . import views

app_name="main"
urlpatterns=[path("",views.home_view,name="home_view"),
             path("post/",views.post_view,name="post_view")]