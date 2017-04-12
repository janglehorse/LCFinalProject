from django import forms

from mealplanner.models import Ingredient, Recipe

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('name', 'text', 'ingredients', 'id')
