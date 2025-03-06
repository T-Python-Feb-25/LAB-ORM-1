from django.urls import path
from . import views

app_name='main'

urlpatterns=[
    path("home/",views.home, name='main'),
    path("new_post/",views.new_post, name='new_post')


]