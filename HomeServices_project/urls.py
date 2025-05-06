from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from HomeServices_project import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HomeServices_app.urls')), 
    path('home/', include('HomeServices_app.urls')),
]

if settings.DEBUG:
    # Serving static and media files in DEBUG mode
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
