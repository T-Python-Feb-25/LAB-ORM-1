from django.urls import path
from . import views
app_name = 'main'

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('detail/<post_id>/', views.detail, name='detail'),
    path('update/<post_id>/', views.update, name='update'),
    path('delete/<post_id>/', views.delete, name='delete')
]