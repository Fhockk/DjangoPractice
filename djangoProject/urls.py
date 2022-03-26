from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import news.views

urlpatterns = [
    path('', include('news.urls')),
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
