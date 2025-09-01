from django.urls import path

from blog.views import index, post_detail, Category_list

urlpatterns = [
    path("", index, name="home"),
    path("post/<int:pk>", post_detail, name="post_detail"),
    path("categories/", Category_list.as_view(),
         name="category_list")
]
