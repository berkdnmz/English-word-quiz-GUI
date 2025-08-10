import csv
import random

class WordManager():
    def __init__(self):
        #Read the word list file
        self.file_path = 'data/words.csv'

        with open(self.file_path, 'r', encoding='utf-8', newline='') as words_file:
            self.words = dict(csv.reader(words_file))


    def select_word(self, count):
        return random.sample(list(self.words.keys()), k=count)