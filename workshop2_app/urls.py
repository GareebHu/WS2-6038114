# workshop2_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('movie_list/', views.movie_list, name='movie_list'),
    path('movie_detail/', views.movie_detail, name='movie_detail'),
]
