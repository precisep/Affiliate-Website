from django.contrib import admin
from django.urls import path, include

from django.conf.urls.static import static

if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL,
                      document_root=settings.STATIC_ROOT)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('affiliate.urls')),
]
