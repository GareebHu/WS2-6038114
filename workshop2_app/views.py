# workshop2_app/views.py
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie
from .serializers import MovieSerializer

@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request):
    movie_name = request.GET.get('movie_name', '')
    movie = get_object_or_404(Movie, name=movie_name)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)
