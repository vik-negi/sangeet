from django.db import models
from django.contrib.auth.models import User
from cloudinary_storage.storage import RawMediaCloudinaryStorage

# Create your models here.

class Song(models.Model):
    name = models.CharField(max_length=200)
    album = models.CharField(max_length=200, null=True)
    language = models.CharField(max_length=200, choices={
        ("Hindi", "Hindi"),
        ("English", "English"),
        ("Punjabi", "Punjabi"),
        ("Kumaoni","Kumaoni"),
        ("korean","korean")
    })
    songImg = models.FileField()
    singer = models.CharField(max_length=200)
    songFile = models.FileField()

    @property
    def songImg_url(self):
        if self.songImg and hasattr(self.songImg, 'url'):
            return self.songImg.url
        else:
            return '\static\img\default_song.png'
    def __str__(self):
        return self.name

class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    playlistName = models.CharField(max_length=200)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=200,choices={
        ('Rock','Rock'),
        ('Pop Music','Pop Music'),
        ("Hip Hop and Rap", 'Hip Hop and Rap'),
        ('Folk','Folk'),
        ('Classical','Classical'),
        ('Techno','Techno'),
        ('Hollywood','Hollywood'),
        ('Bollywood','Bollywood'),
        ('K-POP','K-POP'),
        ('Metal',"Metal"),
    })
    rating = models.FloatField(default=0)
    AlbumImage = models.ImageField(default=None , null=True)

class Favourite(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    isFav = models.BooleanField(default=False)

class Recent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)


class TestModelWithRawFileAndImage(models.Model):
    name = models.CharField(max_length=100)
    raw_file = models.ImageField(upload_to='raw/', blank=True, storage=RawMediaCloudinaryStorage())
    image = models.ImageField(upload_to='images/', blank=True)  # no need to set storage, field will use the default on
