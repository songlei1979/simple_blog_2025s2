from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView

from blog.models import Post, Category


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request,
                  "index.html",
                  {"posts": posts},)

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request,
                  "post_detail.html",
                  {"post": post})

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