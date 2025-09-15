from ckeditor.widgets import CKEditorWidget
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
            "snippet": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter a short summary (snippet)"
            }),
            "category": forms.Select(attrs={
                "class": "form-control"
            }),
            "body": forms.CharField(widget=CKEditorWidget())
        }
