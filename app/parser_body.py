from app.levenshtein_distance import Levenshtein_Distance

class Parser_Body:

    def __init__(self, body):
        self.body = body.lower()
        self.dish = Levenshtein_Distance('dish')
        self.ingredients = Levenshtein_Distance('ingredients')
    
    """
    body:
        dish I want
        all the ingredients I want separated by a comma
    """
    def parse(self):

        aux = self.body.split('\n')

        if len(aux) != 2: return '', ''

        dish, ingredients = '', ''

        for line in aux:

            aux2 = line.split( ' ', 1)
            if len(aux2) == 1:
                word, rest = aux2[0], ''
            else:
                word, rest = aux2

            if self.dish.get_distance_with(word) <= 3:
                dish = rest.strip(' ')
            elif self.ingredients.get_distance_with(word) <= 3:
                ingredients = rest.strip(' ')
            
        dish = dish.replace(' ', '%20')
        ingredients = ','.join([ingredient.strip(' ').replace(' ', '%20') for ingredient in ingredients.split(',')])
        return ingredients, dish
        

        
        