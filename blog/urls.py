from django.urls import path

from blog.views import index, Post_detail, Category_list, Category_detail, Category_update, Post_update

urlpatterns = [
    path("", index.as_view(), name="home"),
    path("post/<int:pk>", Post_detail.as_view(), name="post_detail"),
    path("post_update/<int:pk>", Post_update.as_view(), name="post_update"),
    path("categories/", Category_list.as_view(),
         name="category_list"),
    path("category/<int:pk>",
         Category_detail.as_view(),
         name="category_detail"),
    path("category_update/<int:pk>",
         Category_update.as_view(),
         name="category_update")
]
