from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите email'
    }))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = None
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите имя пользователя' }),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтвердите пароль'}),
        }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'date_completed']
        labels = {
            'title': 'Название задачи',
            'description': 'Описание задачи',
            'date_completed': 'Срок выполнение до',
        }
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4, 'cols': 40}),
            'date_completed': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
