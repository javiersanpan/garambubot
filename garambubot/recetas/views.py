from django.shortcuts import render
import subprocess
from django.http import JsonResponse

def generate_recipe_results(ingredient):
    # Run the Python script to generate the file
    subprocess.run(['python', 'bot.py', ingredient])

def get_recipe_results(request):
    if request.method == 'POST':
        ingredient = request.POST.get('ingredient')
        generate_recipe_results(ingredient)

    with open("/Users/javier/Documents/Garambullo/bot_garambullo/garambubot/recetas/recipe_results.txt", "r") as file:
        results = file.read()

    return JsonResponse({'results': results})
