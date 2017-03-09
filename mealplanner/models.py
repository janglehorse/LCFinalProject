from __future__ import unicode_literals

from django.urls import reverse
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=16)

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add = True)
    text = models.CharField(max_length=500)
    ingredients = models.TextField(max_length=750, null=True)

    #TODO:
    #Create an author field.

    def __str__(self):
        return self.title + " | Text: " + " " + self.text

    #Redirects to detail view after creating a new object
    def get_absolute_url(self):
        return reverse('mealplanner:recipe-detail', kwargs={'pk': self.pk})
