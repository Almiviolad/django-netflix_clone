from django.db import models
import uuid

# Create your models here.

class Genre(models.Model):
    tmdb_id = models.IntegerField(unique=True)
    genre_name = models.CharField(50)

def __str__(self):
    return self.name


class Movie(models.Model):
    movie_id = models.UUIDField(primary_key=True, default=uuid.uuid4, unique=True, editable=False)
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    overview = models.TextField(max_length=700)
    poster = models.ImageField(upload_to='movie_images/')
    popularity = models.DecimalField(decimal_places=3, max_digits=6)
    genres = models.ManyToManyField(Genre)
    def __str__(self):
        return self.title
