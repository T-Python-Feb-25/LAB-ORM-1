from django.urls import path
from . import views

app_name = "main"

urlpatterns = [
    path('',views.home,name='home'),
    path('create/blog',views.create,name="create"),
    path('view/<blog_id>',views.view, name="view"),
    path('update/<blog_id>',views.update,name="update"),
    path('delete/<blog_id>',views.delete,name="delete")
]