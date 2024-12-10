from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from .models import News_post

class News_postForm(ModelForm):
    class Meta:
        model = News_post
        fields = ['title', 'short_description', 'text', 'pub_date', 'user']
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название новости'
            }),
            "short_description": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите краткое описание новости'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите новость'
            }),
            "pub_date": DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local',
                'placeholder': 'Введите дату и время публикации'
            }),
            "user": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя пользователя'
            }),
        }




