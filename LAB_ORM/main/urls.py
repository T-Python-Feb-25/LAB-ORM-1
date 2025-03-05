from django.urls import path
from . import views

app_name="main"

urlpatterns = [
    
    path("", views.Base_view,name="Base_view"),
    path("home/", views.Home_view,name="Home_view")
    
]