from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from blog.forms import PostForm
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
    form_class = PostForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.FILES:
            print("Uploaded files:", self.request.FILES)  # Debug
        print("Updated header_image:", form.instance.header_image)  # Debug
        return response

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
    form_class = PostForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        # form.instance.author = self.request.user
        form.instance.author = User.objects.first()
        return super().form_valid(form)

