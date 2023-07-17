import csv
from django.shortcuts import render
from .models import Recipe

def home(request):
    return render(request, 'recetas/index.html')

def search(request):
    ingredient = request.POST.get('ingredient')
    results = Recipe.objects.filter(ingredients__icontains=ingredient)

    if not Recipe.objects.exists():
        with open('data/recipes.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            recipes = []
            for row in reader:
                recipe = Recipe(title=row['Titulo'], ingredients=row['Ingredientes'], instructions=row['Elaboracion'])
                recipes.append(recipe)
            Recipe.objects.bulk_create(recipes)

    return render(request, 'recetas/search.html', {'ingredient': ingredient, 'results': results})
