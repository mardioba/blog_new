from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from post import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('addcomment/<int:pk>', views.addcomment, name='addcomment'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
