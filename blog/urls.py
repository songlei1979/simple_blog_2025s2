from django.urls import path

from blog.views import index, post_detail

urlpatterns = [
    path("", index, name="home"),
    path("post/<int:pk>", post_detail, name="post_detail")
]
