from Extract_Method_Tools import methods_parse, tools_parse
from ingredient_scrape import RecipeFetcher
from ing_steps import fetch_and_pack
#from transformation1 import *
#from optional_transformation import *
#from transformation2 import *
import json


#if you want to get the human-readable string format of a recipe
def GetRecipe (url):
	#Input recipe is a URL 
	rf = RecipeFetcher()
	results = rf.search_recipes(url)
	#print("Search is Over..Thank you for waiting!")
	new_string = ""
	if not results:
		return "Ooops I think it is not some kind of food"
	else:
		fetch_and_pack(results[0])
		recipe = {}
		with open('recipe.json', 'r') as f:
			recipe = json.load(f)
			new_string += "Alright. So let's start working with the following recipe: \n"

			#print("\nSee below for a human-readable format of your original recipe:\n")
			for key, value in recipe['Recipe'].items():
				if key == "Ingredients":
					new_string += "Ingredients: "
					num = 1
					for ing in value:
						new_string.append("\t" + str(num) + ". ")
						for key1, value1 in ing.items():
							new_string.append("\t\t"+ key1 + ": " + value1)
						num += 1
				if key == "Tools":
					print("Tools: ")
					num = 1
					for tool in value:
						new_string.append("\t" + str(num) + ". " + tool)
						num+=1
				if key == "Methods":
					print("Methods: ")
					num1=1
					num2=1
					for key1, value1 in value.items():
						if key1 == 'Primary_cooking_method':
							new_string.append("\tPrimary cooking method: ")
							for method in value1:
								new_string.append("\t\t" + str(num1) + ". " + method)
								num1 += 1
						if key1 == 'alternative_cooking_method': 
							new_string.append("\tAlternative cooking methods: ")
							for method in value1:
								new_string.append("\t\t" + str(num2) + ". " + method)
								num2 += 1
				if key == "Steps":
					new_string.append("Steps: ")
					num = 1
					for step in value:
						new_string.append("\t" + str(num) + ". " + step + '\n')
						num += 1
	return new_string

#if you want to get the data structure format of the recipe
def JustGetRecipe (url):
	rf = RecipeFetcher()
	results = rf.search_recipes(url)
	#print("Search is Over..Thank you for waiting!")
	if not results:
		return "Ooops I think it is not some kind of food"
	else:
		fetch_and_pack(results[0])
		recipe = {}
		with open('recipe.json', 'r') as f:
			recipe = json.load(f)
	return recipe



def IngredientLookup (my_str):
	#input recipe is a string
	#look to refine keywords 

	str_lst = ["show", "give", "display", "what"] #what else to add here?
	quant_lst = ["how much", "how many"] # add more keywords?
	recipe = {}
	with open('recipe.json', 'r') as f:
		recipe = json.load(f)
	my_ing_lst = recipe['Recipe']['Ingredients']
	my_names = []
	for e in my_ing_lst:
		my_names.append(e['name'])
	#Handling user input requesting to see ingredients list
	if "ingredients" in my_str:
		for e in str_list: #do i even need to iterate through this list?
			if my_str.contains(e): #figure out better keywords strings for parsing input?? see list above
				return my_recipe['Recipe']['Ingredients']

	#Handling user input of asking how much of a specific type of ingredient
	for e in quant_lst: #e is quant strings
		if my_str.contains(e):
			for f in my_names: #f is the name of the ingredient 
				if my_str.contains(f):
					for m in recipe['Recipe']['Ingredients']: #m is a dictionary
						if m['name'] == f:
							return m['quantity']


	#how do i detect ingredient names from a string??
#given a number and a string 
def StepNavigation(my_str, curr_step):
	#recipe is an input string 
	#two cases: relative and specific lookup
	#ordinal_values = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th',]
	#my_recipe = JustGetRecipe(url)
	recipe = {}
	with open('recipe.json', 'r') as f:
		recipe = json.load(f)

	step_values = {'1st': 1, '2nd': 2, '3rd': 3, '4th': 4, '5th': 5, '6th': 6, '7th': 7, '8th': 8, '9th': 9, '10th': 10}
	word_step_values = {'first': 1, 'second': 2, 'third': 3, 'fourth': 4, 'fifth': 5, 'sixth': 6, 'seventh': 7, 'eighth': 8, 'ninth': 9, 'tenth': 10}
	#Case I: specific lookup
	my_ordinal = step_values.keys()
	my_word_ordinal = word_step_values.keys()
	for e in my_ordinal:
		if my_str.contains(e) and my_str.contains("step"):
			my_num = step_values[e]
			return recipe['Ingredients']['Steps'][my_num]  
	for f in my_word_ordinal:
		if my_str.contains(f) and my_str.contains("step"):
			my_num = word_step_values[f]
			return recipe['Ingredients']['Steps'][my_num] 

	#Case II: relative lookup
	num_values = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10}
	my_numbers = num_values.keys()
	moving_back = ["go back", "move back", "take me back"]
	moving_forward = ["go forward", 'move forward', 'take me forward']

	for num in my_numbers:
		if my_str.contains(num):
			for phrase in moving_back:
				if my_str.contains(phrase) and my_str.contains("step"):
					the_num = num_values[num]
					return recipe['Ingredients']['Steps'][curr_step - the_num]

	for num in my_numbers:
		if my_str.contains(num):
			for phrase in moving_forward:
				if my_str.contains(phrase) and my_str.contains("step"):
					the_num = num_values[num]
					return recipe['Ingredients']['Steps'][curr_step + the_num]


	#special case of next and last 
	if my_str.contains("step") and my_str.contains("next"):
		return recipe['Ingredients']['Steps'][curr_step + 1]

	if my_str.contains("step") and my_str.contains("last"):
		return recipe['Ingredients']['Steps'][curr_step - 1]


#Tests
GetRecipe('https://www.allrecipes.com/recipes/16353/salad/green-salads/caesar-salad/?internalSource=hubcard&referringContentType=Search&clickId=cardslot%201')
JustGetRecipe('https://www.allrecipes.com/recipes/16353/salad/green-salads/caesar-salad/?internalSource=hubcard&referringContentType=Search&clickId=cardslot%201')
IngredientLookup("Go over the list of ingredients")
StepNavigation("Go to the next step")
StepNavigation("Go to the third step")
StepNavigation("Go to the last step")
StepNavigation("Go to the 2nd step")




#GetRecipe("https://www.allrecipes.com/recipe/26546/grecian-lamb-caesar-salad/?internalSource=hub%20recipe&referringContentType=Search")







