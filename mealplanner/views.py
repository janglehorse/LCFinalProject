from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from mealplanner.models import Ingredient, Recipe
from mealplanner.forms import RecipeForm, IngredientFormSet, InstructionFormSet

# Create your views here.

class RecipeIndex(View):
    def get(self, request, *args, **kwargs):
        q = Recipe.objects.all()
        template_name = 'mealplanner/recipe_index.html'
        return render(request, template_name, {'object_list': q})

class RecipeCreate(CreateView):
    form_class = RecipeForm
    model = Recipe
    #success_url = reverse('mealplanner:recipe-detail', kwargs={'pk': self.pk})

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = IngredientFormSet()
        instruction_form = InstructionFormSet()
        return self.render_to_response(
            self.get_context_data(form=form,
            ingredient_form=ingredient_form,
            instruction_form=instruction_form)
        )

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = IngredientFormSet(self.request.POST)
        instruction_form = InstructionFormSet(self.request.POST)

        if (form.is_valid() and ingredient_form.is_valid() and instruction_form.is_valid()):
            return self.form_valid(form, ingredient_form, instruction_form)

        else:
            return self.form_invalid(form, ingredient_form, instruction_form)

    def form_valid(self, form, ingredient_form, instruction_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """

        self.object = form.save()
        ingredient_form.instance = self.object
        ingredient_form.save()
        instruction_form.instance = self.object
        instruction_form.save()
        return HttpResponseRedirect(
            reverse('mealplanner:recipe-detail', kwargs={'pk': self.object.pk})
            )

    def form_invalid(self, form, ingredient_form, instruction_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
            ingredient_form=ingredient_form,
            instruction_form=instruction_form)
            )


class RecipeDetail(generic.DetailView):
    model = Recipe
    template_name = 'mealplanner/recipe-detail.html'

class RecipeUpdate(UpdateView):
    form_class = RecipeForm
    model = Recipe
    template_name_suffix = '_update_form'

    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form and its inline formsets.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = IngredientFormSet(instance=self.object)
        instruction_form = InstructionFormSet(instance=self.object)
        return self.render_to_response(
            self.get_context_data(form=form,
            ingredient_form=ingredient_form,
            instruction_form=instruction_form)
        )

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        ingredient_form = IngredientFormSet(self.request.POST, instance=self.object)
        instruction_form = InstructionFormSet(self.request.POST, instance=self.object)

        if (form.is_valid() and ingredient_form.is_valid() and instruction_form.is_valid()):
            return self.form_valid(form, ingredient_form, instruction_form)

        else:
            return self.form_invalid(form, ingredient_form, instruction_form)

    def form_valid(self, form, ingredient_form, instruction_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """

        self.object = form.save()
        ingredient_form.instance = self.object
        ingredient_form.save()
        instruction_form.instance = self.object
        instruction_form.save()
        return HttpResponseRedirect(
            reverse('mealplanner:recipe-detail', kwargs={'pk': self.object.pk})
            )

    def form_invalid(self, form, ingredient_form, instruction_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(
            self.get_context_data(form=form,
            ingredient_form=ingredient_form,
            instruction_form=instruction_form)
            )

class RecipeDelete(DeleteView):
    model = Recipe
    success_url = '/mealplanner'

class IngredientCreate(CreateView):
    model = Ingredient
    fields = [
            'name',
            'quantity',
            'unitOfMeasure',
            'quantity_2',
            'unitOfMeasure_2' ]

class IngredientDetail(generic.DetailView):
    model = Ingredient
    template_name = 'mealplanner/ingredient-detail.html'
