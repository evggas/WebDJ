from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html')

def new(request):
    return render(request, 'main/new.html')

def third(request):
    return render(request, 'main/third.html')

def fourth(request):
    return render(request, 'main/fourth.html')
