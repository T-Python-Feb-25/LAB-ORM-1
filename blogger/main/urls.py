from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_post, name='add_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]