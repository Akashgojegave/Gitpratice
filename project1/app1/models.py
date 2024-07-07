from django.db import models

# Create your models here.
class Anime(models.Model):
    anime_name=models.CharField(max_length=50)
    anime_year=models.CharField(max_length=50)