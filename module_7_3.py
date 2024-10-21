import io
from pprint import pprint
print('Найдёт везде')
print('------------')

class WordsFinder:

    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_names in self.file_names:
            with open(file_names, 'r', encoding='utf-8') as file:
                text = file.read().lower()
                for punctuacion in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    text = text.replace(punctuacion, '')
                words = text.split()
                all_words[file_names] = words
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1
        return result

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}
        for file_name, words in all_words.items():
            result[file_name] = words.count(word)
        return result


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
