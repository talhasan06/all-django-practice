from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Album(models.Model):
    album_name = models.CharField(max_length=255)
    

    def __str__(self):
        return self.album_name
    
class Musician(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    instrument_type = models.CharField(max_length=50)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    album=models.ForeignKey(Album, on_delete=models.CASCADE, related_name='albums')
    release_date = models.DateField(null=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)],default=0)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"