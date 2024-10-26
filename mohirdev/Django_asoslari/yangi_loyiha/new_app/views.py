from django.shortcuts import render, get_object_or_404
from .models import News, Category

def new_list(request):
    new_list = News.published.all()
    context = {
        'new_list': new_list
    }
    return render(request, 'news/new_list.html', context)

def new_detail(request, id):
    news = get_object_or_404(News, pk=id, status=News.Status.PUBLISHED)
    context = {
        'news': news
    }
    return render(request, 'news/new_detail_page.html', context)
