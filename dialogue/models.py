from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Actor(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Movie(models.Model):
    imdb_id = models.CharField(max_length=30,default='0')
    title = models.CharField(max_length=300)
    year = models.IntegerField(default=0)
    image = models.CharField(max_length=1000)
    plot = models.CharField(max_length=1000)
    actors = models.ManyToManyField(Actor)
    runtime = models.IntegerField(default=0)
    genre = models.ManyToManyField(Genre)
    country = models.ManyToManyField(Country)

    def __str__(self):
        return self.title

class Series(models.Model):
    imdb_id = models.CharField(max_length=30,default='0')
    title = models.CharField(max_length=300)
    year = models.IntegerField(default=0)
    image = models.CharField(max_length=1000)
    actors = models.ManyToManyField(Actor)
    genre = models.ManyToManyField(Genre)
    runtime = models.IntegerField(default=0)
    seasons = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Dialogue(models.Model):
    content = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('Date Published')
    movie = models.ForeignKey(Movie)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.content[:20]

