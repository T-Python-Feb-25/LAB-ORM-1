from django.urls import path
from . import views


app_name="blogs"


urlpatterns=[
    path("create/" ,views.create_blog_view ,name="create_blog_view"),
    path("detail/<blog_id>/", views.blog_detail_view, name="blog_detail_view"),
    path("update/<blog_id>/", views.blog_update_view, name="blog_update_view"),
    path("delete/<blog_id>/", views.blog_delete_view, name="blog_delete_view")
]
