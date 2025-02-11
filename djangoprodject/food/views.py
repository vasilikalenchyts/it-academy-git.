from django.shortcuts import render, redirect
from django.template.context_processors import request

from .models import Category, Post, Comment
from django.db.models import F
from .forms import PostAddForm, LoginForm, RegistrationForm, CommentForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.views.generic import  DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView


"""Изменение статьи по кнопке"""
class PostUpdate(UpdateView):
    model = Post
    form_class = PostAddForm
    template_name = 'food/article_add_form.html'


"""Удаление статьи по кнопке"""
class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('index')
    context_object_name = 'post'
    extra_context = {'title': 'Изменить статью'}


"""Смена пароля"""
class UserChangePassword(PasswordChangeView):
    success_url = reverse_lazy('index')


"""Главная страница"""
def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    context = {
        'title' : 'Главная страница',
        'posts' : posts,
        'categories': categories
    }
    return render(request, 'food/index.html', context)


"""Нажатие кнопки категория"""
def category_list(request, pk):
    posts = Post.objects.filter(category_id=pk)
    categories = Category.objects.all()
    context = {
        'title': posts[0].category,
        'posts': posts,
        'categories' : categories
    }
    return render(request, 'food/index.html', context)


"""Страница статьи"""
def post_detail(request, pk):
    article = Post.objects.get(pk=pk)
    Post.objects.filter(pk=pk).update(wathed=F('wathed') + 1)
    ext_post = Post.objects.all().exclude(pk=pk).order_by('-wathed')[:10]
    context = {
        'title' : article.title,
        'post' : article,
        'ext_posts' : ext_post
    }
    return render(request, 'food/article_detail.html', context)



"""Добавление статьи от пользователя без admin"""
def add_post(request):
    if request.method == 'POST':
        form = PostAddForm(request.POST, request.FILES)
        if form.is_valid():
            post = Post.objects.create(**form.cleaned_data)
            post.save()
            return redirect('post_detail', post.pk)
    else:
        form = PostAddForm()

        context = {
            'form' : form,
            'title' : 'Добавить статью'
        }
        return render(request, 'food/article_add_form.html', context)




"""Аутентификация пользователя"""
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Вы успешно вошли в аккаунт')
            return redirect('index')
    else:
        form = LoginForm()

    context = {
        'title': 'Авторизация пользователя',
        'form': form
    }

    return render(request, 'food/login_form.html', context)


"""Выход пользователя"""
def user_logout(request):
    logout(request)
    return redirect('index')


"""Регистрация пользователя"""
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegistrationForm()

    context = {
        'title': 'Регистрация пользователя',
        'form': form
    }
    return render(request, 'food/register.html', context)


"""Страница пользователя"""
def profile(request, user_id):
    user = User.objects.get(pk=user_id)
    posts = Post.objects.filter(author=user)

    context = {
        'user': user,
        'posts': posts
    }
    return render(request, 'food/profilie.html', context)






