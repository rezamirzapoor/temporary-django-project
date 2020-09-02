from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: JsonResponse({'root api': 'http://localhost:8000/api'})),
    path('api/', include('djangosite.api_urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)