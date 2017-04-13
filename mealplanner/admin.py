from django.contrib import admin

from .models import Unit, Ingredient, Recipe

# Register your models here.

admin.site.register(Unit)
admin.site.register(Ingredient)
admin.site.register(Recipe)
