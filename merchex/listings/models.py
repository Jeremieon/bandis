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

    def __str__(self):
        return self.name
class listing(models.Model):
    class Type(models.TextChoices):
        Records ='Records'
        Clothing ='Clothing'
        Posters = 'Posters'
        Miscellaneous='Miscellaneous'
    band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    sold = models.fields.BooleanField(default=True)
    year = models.IntegerField(
        validators=[MinValueValidator(1900),MaxValueValidator(2021)]
    )
    type = models.CharField(choices=Type.choices,max_length=15)
    #jeremy

    def __str__(self):
        return self.title