import csv
from django.shortcuts import render
from .models import Recipe
from django.db.models import Q
import random

def home(request):
    return render(request, 'recetas/index.html')

def search(request):
    if request.method == 'POST':
        ingredient = request.POST['ingredient']
        recipes = Recipe.objects.filter(ingredients__icontains=ingredient)

        # Get three random recipes
        random_recipes = random.sample(list(recipes), 3)

        context = {
            'ingredient': ingredient,
            'recipes': random_recipes,
        }
        return render(request, 'recetas/search.html', context)

    return render(request, 'recetas/search.html')