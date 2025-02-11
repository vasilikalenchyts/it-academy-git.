from django.urls import path
from .views import *

urlpatterns = [
    path('healthyeatinges/', healthyeating, name='healthyeating'),
]