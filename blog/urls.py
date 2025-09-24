from django.urls import path

from blog.views import index, Post_detail, Category_list, Category_detail, Category_update, Post_update, base_view, \
    search, Post_delete, Post_create, ProfileCreateView, ProfileDetailView, ProfileUpdateView, add_comment

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
         name="category_update"),
    path("search/", search, name="search"),
    path("post_delete/<int:pk>",
         Post_delete.as_view(),
         name="post_delete"),
    path("post_create/",
         Post_create.as_view(),
         name="post_create"),
    path("profile/create/", ProfileCreateView.as_view(), name="profile_create"),
    path("profile/<int:pk>/", ProfileDetailView.as_view(), name="profile_detail"),
    path("profile/<int:pk>/update/", ProfileUpdateView.as_view(), name="profile_update"),
    path("add_comment/", add_comment, name="add_comment"),
]
