# workshop2_app/models.py
from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    genre = models.CharField(max_length=255)

    def __str__(self):
        return self.name

