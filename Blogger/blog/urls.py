from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_post, name='add_post'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # Detail view URL
    path('delete/<int:post_id>/', views.delete_post, name='delete_post'),  # New URL for delete
    path('unpublished/', views.unpublished_blogs, name='unpublished_blogs'), # New URL for unpublished posts/blogs
    path('publish/<int:post_id>/', views.publish_post, name='publish_post'),  # Publish blog/post
    path('post/update/<int:post_id>/', views.update_post, name='update_post'), # Update blog/post
]



