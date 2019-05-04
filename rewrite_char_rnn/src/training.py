import random
from dictionary import *

class Training:

	def __init__(self, path):
		self.dictionary = Dictionary(path)
		self.dictionary.load()

	def start(self):
		for i in range(10):
			category, line, category_tensor, line_tensor = self.randomTrainingExample()
			print('category =', category, '/ line =', line)

	def randomChoice(self,l):
	    return l[random.randint(0, len(l) - 1)]

	def randomTrainingExample(self):
		all_categories = self.dictionary.listCategories()
		category = self.randomChoice(all_categories)
		line = self.randomChoice(self.dictionary.getCategoryLines(category))
		category_tensor = torch.tensor([all_categories.index(category)], dtype=torch.long)
		line_tensor = self.dictionary.lineToTensor(line)
		return category, line, category_tensor, line_tensor
