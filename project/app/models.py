from django.db import models


class MusicSheet (models.Model):
    song_Name = models.CharField(max_length=100)
    album_Name = models.CharField(max_length=100)
    artist_Name = models.CharField(max_length=100)
    duration = models.CharField(max_length=7)
    rating = models.CharField(max_length=200)


def __str__(self):
        return self.song_Name

