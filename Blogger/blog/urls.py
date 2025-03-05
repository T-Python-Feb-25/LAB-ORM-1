from django.urls import path
from .views import home, new_post, mode_view, contact, post_detail, post_edit, post_delete

urlpatterns = [
    path('', home, name='home'),
    path('new/', new_post, name='new_post'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/<int:post_id>/edit/', post_edit, name='post_edit'),
    path('post/<int:post_id>/delete/', post_delete, name='post_delete'),
    path('mode/<str:mode>/', mode_view, name='mode_view'),
    path('contact/', contact, name='contact'),
]