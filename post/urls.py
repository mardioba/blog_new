from django.urls import path
from . import views

urlpatterns = [
  path('addcomment/<int:pk>', views.addcomment, name='addcomment'),
]

