from django.contrib import admin

from blog.models import Profile, Category, Post, Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)