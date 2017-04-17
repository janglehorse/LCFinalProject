from __future__ import unicode_literals

from django.urls import reverse
from djfractions.models import DecimalFractionField
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=16)

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add = True)
    text = models.CharField(max_length=255)

    #TODO:
    #Create an author field.

    def __str__(self):
        return self.name + " | Text: " + " " + self.text

    #Redirects to detail view after creating a new object
    def get_absolute_url(self):
        return reverse('mealplanner:recipe-detail', kwargs={'pk': self.pk})

class Ingredient(models.Model):

    CUP = 'CP'
    TABLESPOON = 'TB'
    TEASPOON = 'TS'
    POUND = 'LB'
    OUNCE = 'OZ'
    FLOUNCE = 'FO'
    NONE = 'NA'

    UNIT_OF_MEASURE_CHOICES = (
        (CUP, 'Cup'),
        (TABLESPOON, 'tbs'),
        (TEASPOON, 'tsp'),
        (POUND, 'lb'),
        (OUNCE, 'oz'),
        (FLOUNCE, 'fl oz'),
        (NONE, 'none'),
    )

    name = models.CharField(max_length=55)
    recipe = models.ForeignKey(Recipe)
    quantity = DecimalFractionField(max_digits=4,
                                    decimal_places=2,
                                    limit_denominator=8,
                                    coerce_thirds=True)
    unitOfMeasure = models.CharField(
        max_length=2,
        choices=UNIT_OF_MEASURE_CHOICES,
        default=CUP,
    )

    quantity_2 = DecimalFractionField(max_digits=4,
                                    decimal_places=2,
                                    limit_denominator=8,
                                    coerce_thirds=True)
    unitOfMeasure_2 = models.CharField(
        max_length=2,
        choices=UNIT_OF_MEASURE_CHOICES,
        default=TABLESPOON,
    )


    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('mealplanner:ingredient-detail', kwargs={'pk': self.pk})

class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe)
    number = models.PositiveSmallIntegerField()
    text = models.TextField()

    def __str__(self):
        return self.number + " " + self.text
