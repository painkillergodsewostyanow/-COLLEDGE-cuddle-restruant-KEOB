from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegUser(UserCreationForm):
    username = forms.CharField(label='логин', widget=forms.TextInput(attrs={'class': 'form-input',
                                                                            'placeholder': 'Имя'}))
    password1 = forms.CharField(label='пароль', widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                                  'placeholder': 'Пароль'}))
    password2 = forms.CharField(label='повторите пароль', widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                                'placeholder': 'Повторите пароль'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-input'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-input'})
        }


class LogUser(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input',
                                                                            'placeholder': 'Имя'}))
    password = forms.CharField(label='Логин', widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                            'placeholder': 'Пароль'}))


class AddComment(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'name', 'txt'}

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-input',  'placeholder': 'Имя'}),
            'txt': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Комментарий'})
        }