from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from post.models import Post, Category, Comment
from post.forms import CommentForm
from home.forms import ContactForm
from django.core.paginator import Paginator
from .models import Contact
from django.db.models import Count

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
  paginator = Paginator(posts, 2)
  page_number = request.GET.get('page')
  page_obj = paginator.get_page(page_number)
  
  context = {
    'page_obj': page_obj,
    'post_category': post_category,
    'post_latest': post_latest,
  }
  return render(request, 'pages/blog.html', context)
def post_detail(request, pk, slug):
  post = Post.objects.get(id=pk)
  comment = Comment.objects.filter(post_id=pk, status='Lido')
  total = 0
  for item in comment:
    total += 1
  context = {
    'post': post,
    'comments': comment,
    'total': total
    }
  return render(request, 'pages/post-details.html', context)

def contact(request):
  if request.method == 'POST':
    form = ContactForm(request.POST)
    if form.is_valid():
      data = Contact()
      data.name = form.cleaned_data['name']
      print('Nome:',data.name)
      data.email = form.cleaned_data['email']
      data.subject = form.cleaned_data['subject']
      data.message = form.cleaned_data['message']     
      data.save()
      return HttpResponseRedirect('/contact')
  # else:
    # print("NÃO VALIDADO")
  form = CommentForm
  context = {
    'form': form
  }
  return render(request, 'pages/contact.html', context)

def about(request):
  return render(request, 'pages/about.html')
# MELHORIAS
def cat(request):
  categories = Category.objects.all()
  # Anota cada categoria com o número de postagens associadas a ela
  categories_with_post_count = categories.annotate(num_posts=Count('post'))
  # return render(request, 'pages/cat.html', {'cat': cat})
  return render(request, 'pages/cat.html', {'categories_with_post_count': categories_with_post_count})
def cat_search(request,pk):
  posts = Post.objects.filter(category_id=pk)
  return render(request, 'pages/cat_search.html', {'posts': posts})