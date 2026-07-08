from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    context = {"postagis": Post.objects.all(),}
    return render(request, "blog/index.html", context) 

def post(request, post_id):
    context = {"post": get_object_or_404(Post, id=post_id),}
    return render(request, "blog/post.html", context)