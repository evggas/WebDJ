from django.shortcuts import render, redirect
from .models import News_post
from .forms import News_postForm

def home(request):
    news = News_post.objects.all()
    return render(request, 'news/news.html', {'news': news})

def create_news(request):
    error = None
    if request.method == 'POST':
        form = News_postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = form.errors.as_text()  # Показывает ошибки валидации

    form = News_postForm()
    return render(request, 'news/add_news_post.html', {'form': form, 'error': error})
