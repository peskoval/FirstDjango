from django.db import models

# Create your models here.


class Color(models.Model):
    name = models.CharField(max_length=32, unique=True)


class Item(models.Model):
    name  = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    count = models.PositiveIntegerField() 
    description = models.TextField(max_length=200, default="Базовое описание")
    colors = models.ManyToManyField(to=Color)