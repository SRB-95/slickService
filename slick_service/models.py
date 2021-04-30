from django.db import models

# Create your models here.
class Artist(models.Model):
    artist_name = models.CharField(max_length=100)
    music_style = models.CharField(max_length=100)

    def __str__(self):
        return self.artist_name

class Album(models.Model):
    album_name = models.CharField(max_length=100)
    release_date = models.DateField()
    get_artist = models.ForeignKey(Artist, on_delete = models.CASCADE)

    def __str__(self):
        return self.get_artist.artist_name
    