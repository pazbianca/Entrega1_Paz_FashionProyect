from django.db import models

# Create your models here.

class FashionIcons(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()
    dateOfBirth = models.DateField()
    profession = models.CharField(max_length=40)
    description = models.TextField()



class FashionBrands(models.Model):
    name = models.CharField(max_length=40)
    founder = models.CharField(max_length=40)
    foundedDate = models.DateField(null=True , blank=True)
    headquarters = models.CharField(max_length=40)
    description = models.TextField()

class FashionShows(models.Model):
    name = models.CharField(max_length=40)
    brand = models.CharField(max_length=40)
    collectionPresented = models.CharField(max_length=40)
    fashionCapital = models.CharField(max_length=40)
    date = models.DateField()
    description = models.TextField()



