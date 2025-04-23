from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from HomeServices_project import settings
from . import views  # or from your_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HomeServices_app.urls')),
    path('', views.home), 
]

if settings.DEBUG:
    # Serving static and media files in DEBUG mode
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
