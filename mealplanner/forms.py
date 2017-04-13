from django import forms
from djfractions.forms import DecimalFractionField
from mealplanner.models import Unit, Recipe

class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('name', 'text', 'ingredients', 'id')

class UnitForm(forms.ModelForm):

    class Meta:
        model = Unit
        fields = ('quantity', 'unitOfMeasure')
