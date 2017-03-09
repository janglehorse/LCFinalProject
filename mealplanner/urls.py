from django.conf.urls import url

from . import views

app_name = 'mealplanner'

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^addnew/$', views.RecipeCreate.as_view(), name='addnew' ),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='recipe-detail'),
]
