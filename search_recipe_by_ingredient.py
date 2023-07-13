import pandas as pd
import ast
import random

# Import the necessary libraries

def search_recipe_by_ingredient(ingredient, output_file):
    # Define a function called search_recipe_by_ingredient that takes an ingredient and an output file name as parameters
    
    df = pd.read_csv("recipes.csv")
    # Read the data from the "recipes.csv" file into a DataFrame called df
    
    df.rename(columns={"Unnamed: 0":"index"}, inplace=True)
    # Rename the "Unnamed: 0" column to "index" in the DataFrame
    
    df.set_index("index", inplace=True)
    # Set the "index" column as the index of the DataFrame
    
    df.head(50)
    # Display the first 50 rows of the DataFrame
    
    matching_recipes = []
    # Initialize an empty list to store the matching recipes
    
    for index, row in df.iterrows():
        # Iterate over each row in the DataFrame
        
        ingredientes = ast.literal_eval(row['Ingredientes'])
        # Convert the string representation of ingredients in each row to a list using ast.literal_eval
        
        titulo = row['Titulo']
        # Get the value of the 'Titulo' column for the current row
        
        elaboracion = row['Elaboracion']
        # Get the value of the 'Elaboracion' column for the current row
        
        if any(ingredient in ingrediente for ingrediente in ingredientes):
            # Check if the ingredient parameter is present in any of the ingredients for the current recipe
            matching_recipes.append((titulo, ingredientes, elaboracion))
            # If a match is found, append a tuple containing the title, ingredients, and elaboration to the matching_recipes list
    
    if len(matching_recipes) > 3:
        matching_recipes = random.sample(matching_recipes, 3)
        # If there are more than 3 matching recipes, randomly select 3 recipes from the matching_recipes list
    
    with open(output_file, 'w') as file:
        # Open the output file in write mode
        
        for titulo, ingredientes, elaboracion in matching_recipes:
            # Iterate over each matching recipe
            
            file.write("Titulo: {}\n".format(titulo))
            # Write the title to the file
            
            file.write("Ingredientes: {}\n".format(ingredientes))
            # Write the ingredients to the file
            
            file.write("Elaboracion: {}\n".format(elaboracion))
            # Write the elaboration to the file
            
            file.write("---\n")
            # Write a separator to the file
    
