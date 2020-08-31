from functools import lru_cache

class Levenshtein_Distance:
    def __init__(self, word):
        self.word = word

    def get_distance_with(self, word_b):
        
        @lru_cache(None)
        def get_distance(i, j):
            if i == 0: return j
            if j == 0: return i

            if self.word[i-1] == word_b[j-1]:
                return get_distance(i-1, j-1)
            
            return 1 + min(
                        get_distance(i-1, j),
                        get_distance(i, j-1),
                        get_distance(i-1, j-1)
            )
        return get_distance(len(self.word), len(word_b))


        