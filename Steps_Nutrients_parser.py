from bs4 import BeautifulSoup
import requests

class RecipeFetcher:
    search_base_url = 'https://www.allrecipes.com/search/results/?wt=%s&sort=re'

    def search_recipes(self, keywords):
        search_url = self.search_base_url % (keywords.replace(' ', '+'))

        page_html = requests.get(search_url)
        page_graph = BeautifulSoup(page_html.content)

        return [recipe.a['href'] for recipe in \
                page_graph.find_all('div', {'class': 'grid-card-image-container'})]

    def scrape_recipe(self, recipe_url):
        results = {}
        nutrition = {}

        page_html = requests.get(recipe_url)
        page_graph = BeautifulSoup(page_html.content)

        results["directions"] = [direction.text.strip() for direction in \
                                 page_graph.find_all('span', {'class': 'recipe-directions__list--item'})
                                 if direction.text.strip()]
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
        print("nutrition",nutrition)
        print("directions ",results["directions"])
        print(results)

        return results


# rf = RecipeFetcher()
# meat_lasagna = rf.search_recipes('meat lasagna')[0]
# print(meat_lasagna)
# rf.scrape_recipe(meat_lasagna)
