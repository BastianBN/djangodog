from django.db import models

# Create your models here.

class Breed(models.Model):
    class Size(models.TextChoices):
        TINY = "Tiny"
        SMALL = "Small"
        MEDIUM = "Medium"
        LARGE = "Large"

    class Rating(models.IntegerChoices):
        VERYLOW = 1
        LOW = 2
        MEDIUM = 3
        HIGH = 4
        VERYHIGH = 5

    name = models.CharField(max_length=200)
    size = models.CharField(max_length=20, choices=Size.choices)
    friendliness = models.IntegerField(choices=Rating.choices)
    trainability = models.IntegerField(choices=Rating.choices)
    sheddingamount = models.IntegerField(choices=Rating.choices)
    exerciseneeds = models.IntegerField(choices=Rating.choices)

class Dog(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    favoritefood = models.CharField(max_length=200)
    favoritetoy = models.CharField(max_length=200)
