# Django Blog App Setup Instructions

## 1. Create Models

* Use the provided `models.py` file.
* Ensure all models are properly linked to Django's built-in `User` model using `from django.contrib.auth.models import User`.

## 2. Install Pillow

```bash
pip install Pillow
```

This is required for image upload fields (`ImageField`).

## 3. Set Up Media Directory for Profile and Post Images

In your project settings (`settings.py`), add:

```python
import os
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

In your `urls.py` (project-level), add:

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your existing urls ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

Create the folders:

```bash
mkdir -p media/profile_pics
mkdir -p media/post_headers
```

These will store uploaded images.

## 4. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

## 5. Register Models in `admin.py`

In your app's `admin.py`, register all models:

```python
from django.contrib import admin
from .models import Profile, Post, Comment, Category

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
```

---

## 🔁 Optional: Use This Project with a Virtual Environment

### 1. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Remember change your database settings in settings.py
