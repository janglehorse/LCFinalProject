from django.forms import ModelForm, ModelMultipleChoiceField, CharField, CheckboxSelectMultiple
from django.forms.models import inlineformset_factory

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
