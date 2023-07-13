import search_recipe_by_ingredient


print("¡Hola! escribe un ingrediente y te daré recetas mexicanas basados en eso")

while True: 
    ingrediente = input("Ingrediente: ")
    search_recipe_by_ingredient.search_recipe_by_ingredient(ingrediente, "recipe_results.txt")
    with open("recipe_results.txt") as results:
        results = results.read()
        print(results)
