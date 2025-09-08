from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from blog.models import Post, Category

def base_view(request):
    categories = Category.objects.all()
    return {"categories": categories}

# Create your views here.
class index(ListView):
    model = Post
    template_name = "index.html"

class Post_detail(DetailView):
    model = Post
    template_name = "post_detail.html"

class Post_update(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ["title", "body", "header_image", "category"]
    success_url = reverse_lazy("home")


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

def search(request):
    query = request.POST.get("search_context")
    posts = Post.objects.filter(body__icontains=query)
    print("type", type(posts))
    return render(request,
                  "search.html",
                  {"posts": posts})

class Post_delete(DeleteView):
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")

class Post_create(CreateView):
    model = Post
    template_name = "post_create.html"
    fields = "__all__"
    success_url = reverse_lazy("home")