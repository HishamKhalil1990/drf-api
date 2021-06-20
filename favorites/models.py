from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=256)
    rate = models.FloatField()
    publish = models.IntegerField()
    genre = models.CharField(max_length=256)
    description = models.TextField()
    admin = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self):
        return self.name
