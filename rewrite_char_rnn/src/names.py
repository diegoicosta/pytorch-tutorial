from __future__ import unicode_literals, print_function, division
from io import open
from dictionary import *
from training import *
from network import *

dic = Dictionary('data/names/*.txt')
print(dic.load())

# print(dic.listCategories())



n_hidden = 128
rnn = RNN(len(dic.all_letters), n_hidden, len(dic.listCategories()))

input = dic.lineToTensor('Albert')
hidden = torch.zeros(1, n_hidden)

output, next_hidden = rnn(input[0], hidden)
print(rnn.categoryFromOutput(output, dic.listCategories()))