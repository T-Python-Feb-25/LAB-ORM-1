from django.urls import path
from .import views

app_name='post'
urlpatterns = [
  path('create/',views.create_view,name='create_view'),
]
