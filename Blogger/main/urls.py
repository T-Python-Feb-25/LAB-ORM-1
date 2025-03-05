from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('post/', views.post_view, name='post_view'),

]
