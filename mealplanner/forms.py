from django import forms
from django.forms import ModelForm, ModelMultipleChoiceField, CharField, CheckboxSelectMultiple
from django.forms.models import inlineformset_factory

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from mealplanner.models import ShoppingList, Instruction, Ingredient, Recipe

class ShoppingListForm(ModelForm):

    name = CharField(max_length=55)
    recipes = ModelMultipleChoiceField(
                                    queryset = Recipe.objects.all(),
                                    widget=CheckboxSelectMultiple(),
                                    required=True
                                    )
    class Meta:
        model = ShoppingList
        fields = ('name', 'recipes')

class RecipeForm(ModelForm):

    class Meta:
        model = Recipe
        fields = ('name', 'text')

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=55, help_text='Required. Please enter valid email.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


IngredientFormSet = inlineformset_factory(
                                        Recipe,
                                        Ingredient,
                                        fields=('name',
                                        'category',
                                        'quantity',
                                        'unitOfMeasure',
                                        'quantity_2',
                                        'unitOfMeasure_2')
                                        )
InstructionFormSet = inlineformset_factory(
                                        Recipe,
                                        Instruction,
                                        fields=('number',
                                        'text')
                                        )
