from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
  path("", views.home_view, name="Home"),
  path("create/", views.create_view, name="create"),
  path("details/<post_id>", views.detail_view, name="detail"),
  path("modify/<post_id>", views.modify_view, name="modify"),
  path("delete/<post_id>", views.delete_view, name="delete"),
]