from django.shortcuts import render
from .models import News_post

def home(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})

def create_news(request):
     return render(request, 'news/add_news_post.html')

from django.shortcuts import render

# Create your views here.
