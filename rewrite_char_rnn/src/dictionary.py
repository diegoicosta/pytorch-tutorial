import glob
import unicodedata
import string
import torch
import os

class Dictionary:

	def __init__(self, path):
		self.path = path
		self.all_letters = string.ascii_letters + " .,;'"
		self.category_lines = {}
		self.categories = {}

	def listFiles(self): 
		return glob.glob(self.path)	

	def listCategories(self): 
		return list(self.categories.keys())

	def getCategoryLines(self, category):
		return self.category_lines[category]

	def lineToTensor(self, line):
		tensor = torch.zeros(len(line), 1, len(self.all_letters))
		for li, letter in enumerate(line):
			tensor[li][0][self.all_letters.find(letter)] = 1
		return tensor

	def letterToTensor(self, letter):
		tensor = torch.zeros(1, len(self.all_letters))
		tensor[0][self.__letterToIndex(letter)] = 1
		return tensor

	def load(self):
		self.__loadCategories()
		for category in self.categories:
		    lines = self.__readLines(self.categories[category])
		    self.category_lines[category] = lines

	def __letterToIndex(self, letter):
		return self.all_letters.find(letter)

	def __loadCategories(self):
		for filename in self.listFiles():
		    category = os.path.splitext(os.path.basename(filename))[0]
		    self.categories[category] = filename	

	def __unicodeToAscii(self, s):
	    return ''.join(
	        c for c in unicodedata.normalize('NFD', s)
	        if unicodedata.category(c) != 'Mn'
	        and c in self.all_letters
	    )

	# Read a file and split into lines
	def __readLines(self, filename):
	    lines = open(filename, encoding='utf-8').read().strip().split('\n')
	    return [self.__unicodeToAscii(line) for line in lines]

