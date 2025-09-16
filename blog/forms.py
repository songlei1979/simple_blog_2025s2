from ckeditor.widgets import CKEditorWidget
from django import forms
from .models import Post, Profile


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
            "snippet": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter a short summary (snippet)"
            }),
            "category": forms.Select(attrs={
                "class": "form-control"
            }),
            "body": forms.CharField(widget=CKEditorWidget())
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "profile_pic", "website_url", "github_url"]
        widgets = {
            "profile_pic": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "website_url": forms.URLInput(attrs={"class": "form-control", "placeholder": "Enter your website URL"}),
            "github_url": forms.URLInput(attrs={"class": "form-control", "placeholder": "Enter your GitHub URL"}),
            "bio": forms.CharField(widget=CKEditorWidget())
        }
