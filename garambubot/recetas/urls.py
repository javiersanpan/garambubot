from django.urls import path
from . import views

urlpatterns = [
    path('recipe-results/', views.get_recipe_results, name='recipe_results'),
]