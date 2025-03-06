from . import views
from django.urls import path

app_name = "main"

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add_post, name="add_post")
]