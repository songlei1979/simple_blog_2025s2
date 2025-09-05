from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView

from blog.models import Post, Category


# Create your views here.
class index(ListView):
    model = Post
    template_name = "index.html"

class post_detail(DetailView):
    model = Post
    template_name = "post_detail.html"

class post_update(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ["title", "body", "header_image", "category"]
    success_url = reverse_lazy("index")


class Category_list(ListView):
    model = Category
    template_name = "category_list.html"

class Category_detail(DetailView):
    model = Category
    template_name = "category_detail.html"

class Category_update(UpdateView):
    model = Category
    template_name = "category_update.html"
    fields = ["name"]
    success_url = reverse_lazy("category_list")