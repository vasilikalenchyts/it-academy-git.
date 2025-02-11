from django.shortcuts import render
from django.template.defaultfilters import title

from food.models import Post, Category


def healthyeating(request):
    posts = Post.objects.all()[3:7]
    categories = Category.objects.all()
    context = {
        'title' : 'Правильное питание',
        'posts' : posts,
        'categories': categories
    }
    return render(request, 'healthyeating/healthyeating.html', context)
