from bs4 import BeautifulSoup

import requests

import re


class RecipeFetcher:

    search_base_url = 'https://www.allrecipes.com/search/results/?wt=%s&sort=re'

    def search_recipes(self, keywords): 
        search_url = self.search_base_url %(keywords.replace(' ','+'))

        page_html = requests.get(search_url)
        page_graph = BeautifulSoup(page_html.content)

        return [recipe.a['href'] for recipe in\
               page_graph.find_all('div', {'class':'grid-card-image-container'})]

    def scrape_recipe(self, recipe_url):
        results = {}
        nutrition = {}
        page_html = requests.get(recipe_url)
        page_graph = BeautifulSoup(page_html.content)
        results['ingredients'] = [ingredient.text for ingredient in\
                                  page_graph.find_all('span', {'itemprop':'recipeIngredient'})]

        if(results['ingredients'] == []):
            results['ingredients'] = [ingredient.text.strip("\n").strip() for ingredient in\
                                  page_graph.find_all('span', {'class':'ingredients-item-name'})]

        results['directions'] = [direction.text.strip() for direction in\
                                 page_graph.find_all('span', {'class':'recipe-directions__list--item'})
                                 if direction.text.strip()]

        if(results['directions'] == []):
            direc = []
            for x in page_graph.find_all('li', {'class':'subcontainer instructions-section-item'}):
                s = x.find('p').text.rstrip("\n")
                direc.append(s.strip())
            results['directions'] = direc
            # results['directions'] = [direction.text.strip() for direction in\
            #                      page_graph.find_all('li', {'class':'subcontainer instructions-section-item'})
            #                      if direction.text.strip()]

        results["nutrition"] = nutrition
        results["nutrition"]["calories"] = [ncal.text.strip() for ncal in
                                            page_graph.find_all('span', {'itemprop': 'calories'}) if ncal.text.strip()]
        results["nutrition"]["fat"] = [n.text.strip() for n in page_graph.find_all('span', {'itemprop': 'fatContent'})
                                       if n.text.strip()]
        results["nutrition"]["carbohydrate"] = [ncarbo.text.strip() for ncarbo in
                                                page_graph.find_all('span', {'itemprop': 'carbohydrateContent'}) if
                                                ncarbo.text.strip()]
        results["nutrition"]["sodium"] = [nsodium.text.strip() for nsodium in
                                          page_graph.find_all('span', {'itemprop': 'sodiumContent'}) if nsodium.text.strip()]
        results["nutrition"]["protein"] = [nprotein.text.strip() for nprotein in
                                           page_graph.find_all('span', {'itemprop': 'proteinContent'}) if
                                           nprotein.text.strip()]

        return results
    
    def scrape_nutrition_facts(self, recipe_url):
        results = []

        nutrition_facts_url = '%s/fullrecipenutrition' %(recipe_url)

        page_html = requests.get(nutrition_facts_url)
        page_graph = BeautifulSoup(page_html.content)

        r = re.compile("([0-9]*\.?[0-9]*)([a-zA-Z]+)")

        # for nutrient_row in <ITERATE_OVER_EACH_NUTRIENT>:
        #     nutrient = {}

        #     # Fill out this to scrape and return:
        #     # nutrient['name'], nutrient['amount'],
        #     # nutrient['unit'], nutrient['daily_value']
            
        #     results.append(nutrient)

        return results


# rf = RecipeFetcher()
# meat_lasagna = rf.search_recipes('meat lasagna')[0]
# res = rf.scrape_recipe(meat_lasagna)
# print(res)