from django.contrib import admin

from .models import Recipe, Ingredient, Instruction, ShoppingList

# Register your models here.

admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(Instruction)
admin.site.register(ShoppingList)
