import requests
from box import Box


class Recipes_API:
    
    URL = "http://www.recipepuppy.com/api/?"

    def __init__(self, pages=3):
        self.specific_dish = ""
        self.ingredients = ""
        self.pages = pages
    
    def _get_response(self, ingredients, specific_dish, pages):

        full_url = Recipes_API.URL + f"i={ingredients}&q={specific_dish}&p={pages}"
        response = requests.get(full_url)
        
        if response.status_code != 200:
            return []


        recipes = [Box(recipe) for recipe in response.json()['results']]
        
        return recipes

    def get_recipes(self, ingredients, specific_dish):
        return self._get_response(ingredients, specific_dish, self.pages)


