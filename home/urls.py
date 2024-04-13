from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('blog/', views.blog, name='blog'),
  path('post/<int:pk>/<slug:slug>', views.post_detail, name='post_detail'),
  path('contact/', views.contact, name='contact'),
  path('about/', views.about, name='about'),
  # Melhorias
  path('cat/', views.cat, name='cat'),
  path('cat_search/<int:pk>', views.cat_search, name='cat_search'),
]
