from django.conf.urls import url

from . import views


app_name = 'mealplanner'

urlpatterns = [

    url(r'^signup/$', views.signup, name='signup'),
    url(r'^user/(?P<pk>[0-9]+)/$', views.UserRecipeIndex.as_view(), name='user-recipes'),
    url(r'^$', views.RecipeIndex.as_view(), name='recipe-index'),
    url(r'^addrecipe/$', views.RecipeCreate.as_view(), name='recipe-add' ),
    url(r'^(?P<pk>[0-9]+)/$', views.RecipeDetail.as_view(), name='recipe-detail'),
    url(r'^edit/(?P<pk>[0-9]+)/$', views.RecipeUpdate.as_view(), name='recipe-update'),
    url(r'^delete/(?P<pk>[0-9]+)/$', views.RecipeDelete.as_view(), name='recipe-delete'),
    url(r'^search/results$', views.RecipeSearchListView.as_view(), name='recipe-search'),
    url(r'^lists/$', views.ListIndex.as_view(), name='list-index'),
    url(r'^addlist/$', views.ListCreate.as_view(), name='list-add'),
    url(r'^list/department/(?P<pk>[0-9]+)/$', views.ListByDepartment.as_view(), name='list-department'),
    url(r'^list/recipe/(?P<pk>[0-9]+)/$', views.ListByRecipe.as_view(), name='list-recipe'),
    url(r'^list/edit/(?P<pk>[0-9]+)/$', views.ListUpdate.as_view(), name='list-update'),
    url(r'^list/delete/(?P<pk>[0-9]+)/$', views.ListDelete.as_view(), name='list-delete'),
    url(r'^addingredient/$', views.IngredientCreate.as_view(), name='ingredient-add'),
    url(r'^ingredient/(?P<pk>[0-9]+)/$', views.IngredientDetail.as_view(), name='ingredient-detail'),

]
