from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView
from django.views import generic
from mealplanner.models import Unit, Ingredient, Recipe
from mealplanner.forms import RecipeForm

# Create your views here.

class RecipeIndex(View):
    def get(self, request, *args, **kwargs):
        q = Recipe.objects.all()
        template_name = 'mealplanner/recipe_index.html'
        return render(request, template_name, {'object_list': q})

class RecipeCreate(CreateView):
    form_class = RecipeForm
    model = Recipe
    #fields = ['name', 'text', 'ingredients']

class RecipeDetail(generic.DetailView):
    model = Recipe
    template_name = 'mealplanner/recipe-detail.html'

class IngredientCreate(CreateView):
    model = Ingredient
    fields = ['name', 'unit']

class IngredientDetail(generic.DetailView):
    model = Ingredient
    template_name = 'mealplanner/ingredient-detail.html'
