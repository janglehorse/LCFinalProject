from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.edit import CreateView
from django.views import generic
from mealplanner.models import Recipe

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        q = Recipe.objects.all()
        template_name = 'mealplanner/recipe_list.html'
        return render(request, template_name, {'object_list': q})

class RecipeCreate(CreateView):
    model = Recipe
    fields = ['title', 'text', 'ingredients']

#TODO:
#create DetailView(generic.DetailView)--
#create corresponding template--
#create corresponding urlconf--

class DetailView(generic.DetailView):
    model = Recipe
    template_name = 'mealplanner/detail.html'
    #TODO:
    #logic to make recipe list into dictionary
    #send that logic along to template

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # Get the blog from id and add it to the context
    #     context['some_data'] = 'This is just some data'
    #     return context

    
