
from django.urls import path
from .views import home_view, post_view, post_details_and_edit

urlpatterns = [
    path('', home_view, name='home'),
    path('post/new/', post_view, name='post'), 
    path('post/<int:post_id>/', post_details_and_edit, name='post_details'),
]