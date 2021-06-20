from django.shortcuts import render
from rest_framework import generics
from .models import Movie
from .serializers import FavSerializers

# Create your views here.

class FavoriteList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = FavSerializers

class FavoriteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = FavSerializers