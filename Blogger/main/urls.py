from django.urls import path
from . import views

app_name="main"
urlpatterns=[path("",views.home_view,name="home_view"),
             path("post/",views.post_view,name="post_view"),
             path("detail/<id>/",views.detail_view,name="detail_view"),
            path("update/<id>/",views.update_view,name="update_view"),
             path("delate/<id>/",views.delate_view,name="delate_view"),
             ]