from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from mealplanner.models import Ingredient, Recipe, Instruction

class RecipeForm(ModelForm):

    class Meta:
        model = Recipe
        fields = ('name', 'text')

IngredientFormSet = inlineformset_factory(
                                        Recipe,
                                        Ingredient,
                                        fields=('name',
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
