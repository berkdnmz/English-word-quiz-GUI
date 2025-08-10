import random

class WordManager():
    def __init__(self):
        self.words = {
            "apple": "elma",
            "book": "kitap",
            "banana": "muz",
            "door": "kapı",
            "window": "pencere",
            "dog": "köpek",
            "car": "araba",
            "house": "ev",
            "sun": "güneş",
            "pencil": "kalem"

        }

    def select_word(self, count):
        return random.sample(list(self.words.keys()), k=count)