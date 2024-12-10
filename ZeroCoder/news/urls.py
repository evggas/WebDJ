from django.urls import path
from . import views

urlpatterns = [

	path('', views.home, name='home'),
    path('create_news/', views.create_news, name='create_news'),  # Убедись, что имя совпадает
]