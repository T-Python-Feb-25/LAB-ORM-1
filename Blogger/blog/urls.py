from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('add/', views.add_post, name='add_post'),
    path("details/<blog_id>/", views.details, name="details"),

]
