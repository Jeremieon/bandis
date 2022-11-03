from django.db import models

# Create your models here.

class Band(models.Model):
    name = models.CharField(max_length=150)
    genre = models.CharField()
    biography = models.CharField()
    year_formed = models.IntegerField()
    active = models.fields.BooleanField()
    official_homepage = models.URLField()
class listing(models.Model):
    title = models.CharField(max_length=100)