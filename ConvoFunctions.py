from Extract_Method_Tools import methods_parse, tools_parse
from ingredient_scrape import RecipeFetcher
from ing_steps import fetch_and_pack
#from transformation1 import *
#from optional_transformation import *
#from transformation2 import *
import json


def GetRecipe (recipe):
	#Input recipe is a URL 
	rf = RecipeFetcher()
	results = rf.search_recipes(recipe)
	print("Search is Over..Thank you for waiting!")
	if not results:
		print("Ooops I think it is not some kind of food")
	else:
		fetch_and_pack(results[0])
		recipe = {}
		with open('recipe.json', 'r') as f:
			recipe = json.load(f)
			print("Alright. So let's start working with the following recipe: " + "\n")

			#print("\nSee below for a human-readable format of your original recipe:\n")
			for key, value in recipe['Recipe'].items():
				if key == "Ingredients":
					print("Ingredients: ")
					num = 1
					for ing in value:
						print("\t" + str(num) + ". ")
						for key1, value1 in ing.items():
							print("\t\t"+ key1 + ": " + value1)
						num += 1
				if key == "Tools":
					print("Tools: ")
					num = 1
					for tool in value:
						print("\t" + str(num) + ". " + tool)
						num+=1
				if key == "Methods":
					print("Methods: ")
					num1=1
					num2=1
					for key1, value1 in value.items():
						if key1 == 'Primary_cooking_method':
							print("\tPrimary cooking method: ")
							for method in value1:
								print("\t\t" + str(num1) + ". " + method)
								num1 += 1
						if key1 == 'alternative_cooking_method': 
							print("\tAlternative cooking methods: ")
							for method in value1:
								print("\t\t" + str(num2) + ". " + method)
								num2 += 1
				if key == "Steps":
					print("Steps: ")
					num = 1
					for step in value:
						print("\t" + str(num) + ". " + step + '\n')
						num += 1
	return recipe

def JustGetRecipe (recipe):
	rf = RecipeFetcher()
	results = rf.search_recipes(recipe)
	print("Search is Over..Thank you for waiting!")
	if not results:
		print("Ooops I think it is not some kind of food")
	else:
		fetch_and_pack(results[0])
		recipe = {}
		with open('recipe.json', 'r') as f:
			recipe = json.load(f)
	return recipe



def IngredientLookup (recipe, url):
	#input recipe is a string
	#look to refine keywords 

	my_recipe = JustGetRecipe(url)
	if "ingredients" in recipe:
		return my_recipe['Recipe']['Ingredients']
	#how do i detect ingredient names from a string??
def StepNavigation(recipe, url)
	#recipe is an input string 
	#two cases: relative and specific lookup
	#ordinal_values = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th',]
	my_recipe = JustGetRecipe(url)
	step_values = {'1st': 1, '2nd': 2, '3rd': 3, '4th': 4, '5th': 5, '6th': 6, '7th': 7, '8th': 8, '9th': 9, '10th': 10}
	my_ordinal = step_values.keys()
	for e in my_ordinal:
		if recipe.contains(e):
			my_num = step_values[e]
			return my_recipe['Ingredients']['Steps'][my_num]



#GetRecipe("https://www.allrecipes.com/recipe/26546/grecian-lamb-caesar-salad/?internalSource=hub%20recipe&referringContentType=Search")








