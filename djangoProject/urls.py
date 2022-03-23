from django.contrib import admin
from django.urls import path, include

import news.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('news/', include('news.urls')),
]
