from rest_framework import serializers
from .models import Movie

class FavSerializers(serializers.ModelSerializer):
    class Meta:
        model  = Movie
        fields = ('id','name','rate','publish','genre','description','admin')