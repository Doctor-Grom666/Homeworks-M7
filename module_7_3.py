import string


class WordsFinder:
    file_names = []

    def __init__(self, *args):
        for i in args:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                words = []
                for line in file:
                    punct = line.lower().translate(str.maketrans('', '', string.punctuation))
                    words += punct.split()
                    all_words[name] = words
        return all_words

    def find(self, word):
        dict_ = {}
        for name, words in self.get_all_words().items():
            for i in words:
                if word.lower() == i.lower():
                    dict_[name] = words.index(i) + 1
        return dict_

    def count(self, word):
        dict_ = {}
        for name, words in self.get_all_words().items():
            count = 0
            for i in words:
                if word.lower() == i.lower():
                    count += 1
            dict_[name] = count
        return dict_


finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))
