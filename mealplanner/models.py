from __future__ import unicode_literals

from django.urls import reverse
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=16)

class Ingredient(models.Model):
    CUP = 'CP'
    TABLESPOON = 'TB'
    TEASPOON = 'TS'
    POUND = 'LB'
    OUNCE = 'OZ'
    FLOUNCE = 'FO'

    UNIT_OF_MEASURE_CHOICES = (
        (CUP, 'Cup'),
        (TABLESPOON, 'tbs'),
        (TEASPOON, 'tsp'),
        (POUND, 'lb'),
        (OUNCE, 'oz'),
        (FLOUNCE, 'fl oz'),
    )

    name = models.CharField(max_length=35)
    quantity = models.IntegerField(default=1)
    unitOfMeasure = models.CharField(
        max_length=2,
        choices=UNIT_OF_MEASURE_CHOICES,
        default=CUP,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('mealplanner:ingredient-detail', kwargs={'pk': self.pk})

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add = True)
    text = models.CharField(max_length=500)
    ingredients = models.ManyToManyField(Ingredient)

    #TODO:
    #Create an author field.

    def __str__(self):
        return self.title + " | Text: " + " " + self.text

    #Redirects to detail view after creating a new object
    def get_absolute_url(self):
        return reverse('mealplanner:recipe-detail', kwargs={'pk': self.pk})
