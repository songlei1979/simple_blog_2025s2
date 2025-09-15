# Django Blog Application

This is a simple blog project built with Django. It allows users to create, update, and manage blog posts with images, categories, and snippets.

---

## 📝 PostForm (forms.py)

We use a custom `PostForm` to make the blog post form more user-friendly and styled with Bootstrap.

```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "title_tag", "header_image", "body", "snippet", "category"]

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the post title"
            }),
            "title_tag": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the SEO title tag"
            }),
            "header_image": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),
            "body": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 5,
                "placeholder": "Write your post content here..."
            }),
            "snippet": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter a short summary (snippet)"
            }),
            "category": forms.Select(attrs={
                "class": "form-control"
            }),
        }
```

### Field explanations
- **title** → main post title (text input with Bootstrap styling).  
- **title_tag** → meta/SEO title tag for better search engine optimization.  
- **header_image** → image upload field with a "Clear" option (thanks to `ClearableFileInput`).  
- **body** → main content of the blog post (textarea with 5 rows).  
- **snippet** → short summary of the post (used in previews).  
- **category** → dropdown list to assign a category.  

---

## ⚙️ Views (views.py)

We use Django class-based views with the custom `PostForm`.

### Create a Post
```python
class Post_create(CreateView):
    model = Post
    template_name = "post_create.html"
    form_class = PostForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        # Assigns an author before saving the post.
        # Currently set to the first user in the database for testing.
        # Replace with: form.instance.author = self.request.user
        form.instance.author = User.objects.first()
        return super().form_valid(form)
```

- Uses `PostForm` for clean Bootstrap styling.  
- Automatically assigns an **author** to the post.  
  - (In production, replace `User.objects.first()` with `self.request.user`).  
- Redirects to `home` after successful creation.  

---

### Update a Post
```python
class Post_update(UpdateView):
    model = Post
    template_name = "post_update.html"
    form_class = PostForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        response = super().form_valid(form)
        if self.request.FILES:
            print("Uploaded files:", self.request.FILES)  # Debugging uploaded files
        print("Updated header_image:", form.instance.header_image)  # Debug current image
        return response
```

- Also uses `PostForm` for consistent styling.  
- Prints debug information when files are uploaded.  
- Keeps the old image unless a new one is uploaded or cleared.  

---

## 🚀 Getting Started

Follow these steps to set up the project locally:

### 1. Clone the repository
```bash
git clone https://github.com/songlei1979/simple_blog_2025s2
cd simple_blog_2025s2
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up the database

This project is configured to use **PostgreSQL**.  
In your `settings.py`, update the `DATABASES` section with **your own database name, user, password, and host**.

Example configuration:

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": "ep-dark-term-adu1n8b7-pooler.c-2.us-east-1.aws.neon.tech",  # change this to your DB url
        "PORT": 5432,
        "NAME": "neondb",          # change this to your DB name
        "USER": "neondb_owner",    # change this to your DB user
        "PASSWORD": "your_password_here",  # change this to your DB password
    }
}
```

---

### 5. Run migrations
```bash
python manage.py migrate
```

### 6. Create a superuser
```bash
python manage.py createsuperuser
```

### 7. Run the development server
```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to see the project in action.

---

## ✅ Notes
- Uploaded images are stored in `/media/post_headers/`.  
- Make sure `MEDIA_URL` and `MEDIA_ROOT` are set in `settings.py`.  
- Don’t forget to collect static files before deployment:
```bash
python manage.py collectstatic
```
