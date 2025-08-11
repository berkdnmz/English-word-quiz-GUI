import csv
import random
import sys


class WordManager():
    def __init__(self):
        self.file_path = 'data/words.csv'
        self.words = self.check_words_file()

    # Read the word list file
    def check_words_file(self):
        #try-except
        try:
            with open(self.file_path, 'r', encoding='utf-8', newline='') as words_file:
                self.words = dict(csv.reader(words_file))
                self.words.pop("ENGLISH",None)
                self.words.pop("english", None)
                self.words.pop("English", None)

                if not self.words:
                    print("CSV file is empty!")
                    sys.exit(1)
        except FileNotFoundError:
            print(f"Error: File not found at {self.file_path}")
            sys.exit(2)
        except PermissionError:
            print(f"Error: No permission to access the file: {self.file_path}")
            sys.exit(3)
        except UnicodeDecodeError:
            print("Error: File encoding is not compatible")
        except Exception as e:
            print(f"An unexpected error occurred: {type(e).__name__} - {e}")
        return self.words

    def select_word(self, count):
        return random.sample(list(self.words.keys()), k=count)