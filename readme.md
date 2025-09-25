# Django Blog Application with CKEditor and User Profiles

This is a simple blog project built with Django.  
It allows users to create, update, and view blog posts with categories, snippets, **rich text editing** using **CKEditor**, and user profiles.  

---

## 📝 Features
- Create, update, and delete blog posts  
- Upload and display **header images**  
- Rich text editor for post body using **CKEditor**  
- Support for uploading and embedding images in the editor  
- Category and snippet support  
- **User profiles** with bio, profile picture, website, and GitHub  
- Conditional menu options for Create/Update Profile  
- Bootstrap-styled forms for clean UI  

---

## ⚙️ CKEditor Setup

### 1. Install django-ckeditor
```bash
pip install django-ckeditor
```

### 2. Add to INSTALLED_APPS
In `settings.py`:

```python
INSTALLED_APPS = [
    ...
    "ckeditor",
    "ckeditor_uploader",
]
```

---

## 📂 Static & Media Settings

Add this to your `settings.py`:

```python
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Static files
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Media files (for uploads)
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# CKEditor upload path
CKEDITOR_UPLOAD_PATH = "uploads/"
```

---

## 🔗 URLs

In your project’s `urls.py`, add:

```python
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
    path("ckeditor/", include("ckeditor_uploader.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

---

## 🖊️ PostForm with CKEditor

Update `forms.py`:

```python
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget())  # Rich text editor

    class Meta:
        model = Post
        fields = ["title", "title_tag", "header_image", "body", "snippet", "category"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the post title"}),
            "title_tag": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter the SEO title tag"}),
            "header_image": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "snippet": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter a short summary (snippet)"}),
            "category": forms.Select(attrs={"class": "form-control"}),
        }
```

---

## 👤 ProfileForm with CKEditor

```python
from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Profile

class ProfileForm(forms.ModelForm):
    bio = forms.CharField(widget=CKEditorWidget())  # Rich text editor for bio

    class Meta:
        model = Profile
        fields = ["bio", "profile_pic", "website_url", "github_url"]
        widgets = {
            "profile_pic": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "website_url": forms.URLInput(attrs={"class": "form-control", "placeholder": "Enter your website URL"}),
            "github_url": forms.URLInput(attrs={"class": "form-control", "placeholder": "Enter your GitHub URL"}),
        }
```

---

## 🏗️ Views

### Post Views
```python
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from .models import Post, Profile
from .forms import PostForm, ProfileForm

class Post_create(CreateView):
    model = Post
    form_class = PostForm
    template_name = "post_create.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.instance.author = User.objects.first()  # Replace with self.request.user
        return super().form_valid(form)

class Post_update(UpdateView):
    model = Post
    form_class = PostForm
    template_name = "post_update.html"
    success_url = reverse_lazy("home")

class Post_detail(DetailView):
    model = Post
    template_name = "post_detail.html"
```

---

### Profile Views
```python
from django.views.generic import CreateView, DetailView, UpdateView

class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = "profile_create.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
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

    def get_queryset(self):
        return Profile.objects.filter(user=self.request.user)
```

---

## 🎨 Templates

### Navbar Logic (Base.html)
```html
{% if user.is_authenticated %}
    <li class="nav-item">
        <form method="post" action="{% url 'logout' %}">
            {% csrf_token %}
            <button class="btn btn-link">Logout</button>
        </form>
    </li>
    {% if user.profile %}
        <li class="nav-item">
            <a class="nav-link" href="{% url 'profile_update' user.profile.pk %}">Edit Profile</a>
        </li>
    {% else %}
        <li class="nav-item">
            <a class="nav-link" href="{% url 'profile_create' %}">Create Profile</a>
        </li>
    {% endif %}
{% else %}
    <li class="nav-item"><a class="nav-link" href="{% url 'login' %}">Login</a></li>
    <li class="nav-item"><a class="nav-link" href="{% url 'register' %}">Register</a></li>
{% endif %}
```

---

### Post Detail Template (show profile link if available)
```html
<a href="{% url 'post_detail' post.pk %}" class="link-info">
    {{ post.title }}
</a>
{% if post.author.profile %}
    <a href="{% url 'profile_detail' post.author.profile.pk %}">{{ post.author.username }}</a>
{% else %}
    <p>{{ post.author.username }} has no profile</p>
{% endif %}
```

---

### Profile Create
```html
{% extends "Base.html" %}
{% block title %}Create Profile{% endblock %}
{% block content %}
<div class="container mt-4">
    <h2>Create Your Profile</h2>
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.media }}
        {{ form.as_p }}
        <button type="submit" class="btn btn-success">Create</button>
    </form>
</div>
{% endblock %}
```

---

### Profile Detail
```html
{% extends "Base.html" %}
{% block title %}Profile{% endblock %}
{% block content %}
<div class="container mt-4">
    <h2>{{ profile.user.username }}'s Profile</h2>
    {% if profile.profile_pic %}
        <img src="{{ profile.profile_pic.url }}" class="img-thumbnail mb-3" width="200">
    {% endif %}
    <div class="mb-3">
        <strong>Bio:</strong>
        <div>{{ profile.bio|safe }}</div>
    </div>
    {% if profile.website_url %}
        <p><strong>Website:</strong> <a href="{{ profile.website_url }}" target="_blank">{{ profile.website_url }}</a></p>
    {% endif %}
    {% if profile.github_url %}
        <p><strong>GitHub:</strong> <a href="{{ profile.github_url }}" target="_blank">{{ profile.github_url }}</a></p>
    {% endif %}
</div>
{% endblock %}
```

---

### Profile Update
```html
{% extends "Base.html" %}
{% block title %}Update Profile{% endblock %}
{% block content %}
<div class="container mt-4">
    <h2>Update Profile</h2>
    <form method="post" enctype="multipart/form-data">
        {% csrf_token %}
        {{ form.media }}
        {{ form.as_p }}
        <button type="submit" class="btn btn-primary">Update</button>
    </form>
</div>
{% endblock %}
```

---

## ✅ Notes
- Each user can create **only one profile** (because of `OneToOneField`).  
- Navbar dynamically shows **Create Profile** or **Edit Profile**.  
- Profile links are shown next to posts if the author has a profile.  
- `bio` and `body` fields both use **CKEditor** for rich text editing.  
- Uploaded profile pics → `/media/profile_pics/`.  
- Uploaded CKEditor images → `/media/uploads/`.  

