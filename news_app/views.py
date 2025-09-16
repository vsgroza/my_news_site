from django.shortcuts import render, get_object_or_404
from .models import News

def index(request):
    news = News.objects.all()
    return render(request, 'news_app/index.html', {'news': news})

def view_news(request, news_id):
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news_app/view_news.html', {'news_item': news_item})