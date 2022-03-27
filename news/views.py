from django.shortcuts import render
from django.http import HttpResponse

from .models import News, Category


def index(request):
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': 'The List of news',
    }
    return render(request, 'news/index.html', context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    return render(request, 'news/category.html', {'news': news, 'category': category})



