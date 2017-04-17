from django.conf.urls import url

from . import views

app_name = 'mealplanner'

urlpatterns = [
    url(r'^$', views.RecipeIndex.as_view(), name='recipe-index'),
    url(r'^addrecipe/$', views.RecipeCreate.as_view(), name='recipe-add' ),
    url(r'^(?P<pk>[0-9]+)/$', views.RecipeDetail.as_view(), name='recipe-detail'),
    url(r'^addingredient/$', views.IngredientCreate.as_view(), name='ingredient-add'),
    url(r'^ingredient/(?P<pk>[0-9]+)/$', views.IngredientDetail.as_view(), name='ingredient-detail'),

]
