from django.shortcuts import render
from food.models import Post, Category

"""Главная страница"""
def myfavorite(request):
    posts = Post.objects.all()[1:5]
    categories = Category.objects.all()
    context = {
        'title' : 'Любимые блюда',
        'posts' : posts,
        'categories': categories
    }
    return render(request, 'myfavoritedishes/myfavoritedishes.html', context)
