from django.shortcuts import render
from .models import Post
from home.models import Tag


def blog_home(request):
    tags = Tag.objects.all()
    posts = Post.objects.all()
    context = {
        'posts': posts,
        'tags': tags,
    }
    return render(request, 'blog.html', context)