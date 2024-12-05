from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('new', views.new, name='page2'),
    path('third', views.third, name='page3'),
    path('fourth', views.fourth, name='page4')
]

