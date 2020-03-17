import re

unit_white_list = ['teaspoon', 'tablespoon', 'fluid ounce', 'ounce', 'cup', 'pint', 'quart', 'gallon',
'milliliter', 'liter', 'pound', 'milligram', 'kilogram', 'gram', 'millimeter', 'centimeter', 'meter', 'inch', 'to taste']

bad_phrase = ['to taste', '(', ')', '/', '\\n', ', or']

preparations = ['chopped', 'minced', 'diced', 'grated', 'sliced', 'halved']

def make_ing_list(ingredients):
	ingredient_list = []
	for ing in ingredients:
		ing_obj = ing_parse(ing)
		ingredient_list.append(ing_obj)
	return ingredient_list

def ing_parse(ingredient):
	x = {}
	temp = re.findall(r'\d*\/\d*|\d*\.\d+|\d+', ingredient)
	num = ''
	if len(temp) == 0:
		num = ''
	elif len(temp) > 1:
		running = 1
		for i in temp:
			n = num_check(str(i))
			running = running * n
		num = str(running)
	else:
		num = str(num_check(list(map(str, temp))[0]))

	x["quantity"] = num;
	for s in temp:
		ingredient = ingredient.replace(s,'')
	# ingredient = ingredient.strip()

	for u in unit_white_list:
		if u in ingredient:
			x["measurement"] = u
			plural = u + "s"
			if plural in ingredient:
				ingredient = ingredient.replace(plural,'')
				# ingredient = ingredient.strip()
			else:
				ingredient = ingredient.replace(u,'')
				# ingredient = ingredient.strip()
			break

	for p in preparations:
		if p in ingredient:
			x["preparation"] = p
			ingredient = ingredient.replace(p,'')
			break

	pattern = '[0-9]'
	ingredient = re.sub(pattern, '', ingredient)

	for b in bad_phrase:
		if b in ingredient:
			ingredient = ingredient.replace(b,'')

	ingredient = ingredient.strip()

	x["name"] = ingredient
	return x;

def num_check(num):
	if '/' in num:
		s = num.split('/')
		x = int(s[0])/int(s[1])
		return x
	else:
		return float(num)