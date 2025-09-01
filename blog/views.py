from django.shortcuts import render

from blog.models import Post


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
