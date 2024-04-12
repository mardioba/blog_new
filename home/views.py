from django.shortcuts import render, HttpResponse
from post.models import Post, Category
def index(request):
  post_random = Post.objects.order_by('?')[:4]
  post_latest = Post.objects.order_by('id')[:3]
  post_category = Category.objects.order_by('title').all()
  context = {
    'post_random': post_random,
    'post_latest': post_latest,
    'post_category': post_category
  }
  return render(request, 'pages/index.html', context)
def blog(request):
  posts = Post.objects.all()
  post_latest = Post.objects.order_by('id')[:3]
  post_category = Category.objects.order_by('title').all()
  context = {
    'posts': posts,
    'post_category': post_category,
    'post_latest': post_latest
  }
  return render(request, 'pages/blog.html', context)