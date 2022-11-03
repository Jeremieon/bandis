from django.db import models

# Create your models here.

class Band(models.Model):
    name = models.CharField(max_length=150)
class listing(models.Model):
    title = models.CharField(max_length=100)