from django.db import models
from django.contrib.auth.models import User

class Songs(models.Model):
    song_artist = models.CharField(max_length = 50)
    song_track = models.TextField()
    song_genre = models.CharField(max_length = 50)
    song_hits = models.IntegerField()
    static_id = models.ForeignKey('Songs_static')



class Songs_static(models.Model):
    static_album = models.CharField(max_length = 50)
    static_release_date = models.DateField()
    static_release_label = models.CharField(max_length = 50)


class Playlist(models.Model):
    u_id = models.ForeignKey(User)
    s_id = models.ForeignKey('Songs')



