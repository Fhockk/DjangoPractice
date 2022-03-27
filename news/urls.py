from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path("cat/<int:category_id>/", get_category, name='category'),
    path("news/<int:news_id>/", view_news, name='view_news'),
]
