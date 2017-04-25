from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views import generic
from mealplanner.models import ShoppingList, Ingredient, Recipe
from django.contrib.auth.models import User
from mealplanner.forms import SignUpForm, ShoppingListForm, RecipeForm, IngredientFormSet, InstructionFormSet
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('mealplanner:recipe-index')
    else:
        form = SignUpForm()
    return render(request, 'mealplanner/signup.html', {'form':form})


class RecipeIndex(ListView):

    model = Recipe
    title = 'All Recipes'
    template_name = 'mealplanner/recipe_index.html'

    # def get(self, request, *args, **kwargs):
    #     q = Recipe.objects.all()
    #     template_name = 'mealplanner/recipe_index.html'
    #     return render(request, template_name, {'object_list': q})


class UserRecipeIndex(generic.DetailView):

    model = User
    title = 'Recipes by '
    template_name = 'mealplanner/user_recipe_index.html'

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(UserRecipeIndex, self).get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['object_list'] = User.objects.get(self.kwargs['pk'])
    #     return context

    # def get(self, request, *args, **kwargs):
    #     q = Recipe.objects.filter(author_id=self.kwargs['pk'])
    #     template_name = 'mealplanner/recipe_index.html'
    #     return render(request, template_name, {'object_list': q})

class RecipeCreate(LoginRequiredMixin, CreateView):
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
        #obj = form.save(commit=False)
        #obj.author = self.request.user
        #...
        # obj.save
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
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
    template_name = 'mealplanner/recipe_detail.html'

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

class RecipeSearchListView(generic.ListView):

    model = Recipe
    context_object_name = 'search_results'
    template_name = 'mealplanner/search_results.html'

    def get_queryset(self):
        #result = super(RecipeSearchListView, self).get_queryset()
        query = self.request.GET.get('q')
        if not query == "":
            result = Recipe.objects.filter(name__contains=query)
        else:
            result = None
        return result

class ListCreate(CreateView):
    form_class = ShoppingListForm
    model = ShoppingList

class ListByDepartment(generic.DetailView):
    model = ShoppingList
    #template_name = 'mealplanner/shoppinglist_detail.html'
    template_name = 'mealplanner/shoppinglist_by_department.html'

class ListByRecipe(generic.DetailView):
    model = ShoppingList
    template_name = 'mealplanner/shoppinglist_by_recipe.html'

class ListIndex(generic.base.TemplateView):

    template_name = "mealplanner/list_index.html"

    def get_context_data(self, **kwargs):
        context = super(ListIndex, self).get_context_data(**kwargs)
        context['list_index'] = ShoppingList.objects.all()
        return context

class ListUpdate(UpdateView):
    form_class = ShoppingListForm
    model = ShoppingList
    template_name_suffix = '_update_form'

class ListDelete(DeleteView):
    model = ShoppingList
    success_url = '/mealplanner/lists'

class IngredientCreate(CreateView):
    model = Ingredient
    fields = [
            'name',
            'quantity',
            'unitOfMeasure',
            'quantity_2',
            'unitOfMeasure_2',]

class IngredientDetail(generic.DetailView):
    model = Ingredient
    template_name = 'mealplanner/ingredient-detail.html'
