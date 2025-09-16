from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from blog.forms import PostForm, ProfileForm
from blog.models import Post, Category, Profile


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
        form.instance.author = self.request.user
        return super().form_valid(form)

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request,
                  "registration/register.html",
                  {"form": form})


class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = "profile_create.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        # Assign current logged-in user to the profile
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profile_detail.html"
    context_object_name = "profile"


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = "profile_update.html"
    success_url = reverse_lazy("home")