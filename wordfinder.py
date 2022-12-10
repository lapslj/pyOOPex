"""Word Finder: finds random words from a dictionary."""
from random import randint
def file_to_dict(path):
    file = open(path)
    line_list = []
    for line in file:
        fixline = line.replace("\n","")
        line_list.append(fixline)
    return line_list

class WordFinder:
    """
    Given a path to a txt file that is a list of words, creates a dictionary
    of the words in that txt file. self.random() returns a random word from
    that dictionary
    """

    def __init__(self,path):
        self.path = path
        self.list = file_to_dict(path)

    def random(self):
        wordno = randint(0,len(self.list))
        return self.list[wordno]

class SpecialWordFinder(WordFinder):
    """
    Extension of WordFinder class that filters out empty lines and lines beginning with "#"
    """
    def __init__(self,path):
        super().__init__(path)
        ignore = ["#"]
        self.filterlist = [word for word in self.list if len(word) > 0]
        self.filterlist = [word for word in self.filterlist if word[0] != "#"] 
    
    def random(self):
        wordno = randint(0,len(self.filterlist))
        return self.filterlist[wordno]


    ...
