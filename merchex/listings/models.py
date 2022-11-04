from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

# Create your models here.

class Band(models.Model):
    class Genre(models.TextChoices):
        HIP_HOP ='HH'
        SYNTH_POP ='SP'
        ALTERNATIVE_ROCK = 'AR'
    name = models.CharField(max_length=150)
    genre = models.CharField(choices=Genre.choices,max_length=5)
    biography = models.CharField(max_length=1000)
    year_formed = models.IntegerField(
        validators=[MinValueValidator(1900),MaxValueValidator(2021)]
    )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.URLField()
class listing(models.Model):
    class Type(models.TextChoices):
        Records ='Rec'
        Clothing ='Cloth'
        Posters = 'poster'
        Miscellaneous='other'
   
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    sold = models.IntegerField()
    year = models.DateTimeField()
    type = models.CharField(choices=Type.choices,max_length=15)
    #jeremy