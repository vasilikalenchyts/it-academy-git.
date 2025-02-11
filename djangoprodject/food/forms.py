from django import forms
from .models import Post, Comment
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


"""Добавление новой статьи от пользователя"""
class PostAddForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'photo', 'category')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'photo': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

"""Аутентификация пользователя """
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя', max_length=100,
                               widget=forms.TextInput(attrs={'class' : 'form-control'}))

    password = forms.CharField(label='Пароль', max_length=100,
                               widget=forms.PasswordInput(attrs={'class': 'form-control'}))


"""Регистрация пользователя"""
class RegistrationForm(UserCreationForm):


    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class': 'form-control',
                                                                            'placeholder': 'Имя пользователя'}))

    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                           'placeholder': 'Электронная почта'}))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                             'placeholder': 'Пароль'}))

    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Подтвердите пароль'}))


"""Форма для написания комментарий"""
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control',
                                                                  'placeholder': 'Текст вашего комментария'})
        }
