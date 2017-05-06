from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=300)
    year = models.IntegerField(default=0)
    image = models.CharField(max_length=1000)

    def __str__(self):
        return self.title

class Dialogue(models.Model):
    content = models.CharField(max_length=1000)
    pub_date = models.DateTimeField('Date Published')
    movie = models.ForeignKey(Movie)

    def __str__(self):
        return self.content[:20]
