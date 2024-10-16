from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()

class Movie(models.Model):
    title = models.CharField(max_length=150)
    director = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=30)
    lead_actor = models.ForeignKey(Actor, on_delete=models.CASCADE)