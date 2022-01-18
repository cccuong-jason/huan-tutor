import numpy as np
import pandas as pd
import os.path

scriptpath = os.path.dirname(__file__)
filename = os.path.join(scriptpath, 'TeamPY4DS_Apyori.csv')
dataset = pd.read_csv(filename, sep=',')

# add column items_buy whose rows are list of items from items_base
dataset['items_buy'] = dataset['items_base'].str.split()

# get distinct item in dataset of items_buy
list_items = []
for row in dataset['items_buy']:
    for item in row:
        if item not in list_items:
            list_items.append(item)
list_items = np.sort(list_items)

# numbering for each item in list
dict_items = {}
for i in range(0, len(list_items)):
    dict_items[i] = list_items[i]


def Suggest(a):
  X=[]
  Y=[]
  a = list(np.sort(a))
  for i in range(1, len(dataset['items_buy'])):
    b = list(np.sort(dataset['items_buy'][i]))
    if a == b: 
      X.append(dataset['items_add'][i])
      Y.append(dataset['confidence'][i])
  if len(a)>=2:
    for i in range(0, len(a)):
      for j in range(0, len(dataset['items_buy'])):
        b = dataset['items_buy'][j]
        if a[i] in b: 
          X.append(dataset['items_add'][j])
          Y.append(dataset['confidence'][j])
  for i in range(0, len(a)):
    while a[i] in X: 
      X.remove(a[i])
      Y.remove(Y[i])
  Z = [x for _, x in sorted(zip(Y, X))]
  for i in range(len(Z)):
    Z[i] = Z[i].split()
  A = []
  for i in Z:
    A.extend(i)
  M = np.unique(A, return_index=True)[1]
  return [A[i] for i in sorted(M, reverse=True)][::5]

# def InputNumber(a, b):
#   n = input(" ")
#   if n.isnumeric():
#       if a <= int(n) <= b:
#           return int(n)
#       else:
#           print('Wrong input, try again: ')
#           InputNumber(a, b)
#   elif '-' in n:
#       print('Wrong input, try again: ')
#       InputNumber(a, b)
#   else:
#     t = n.strip(' ').rstrip(' ')
#     if a.isnumeric():
#       return int(t)
#     else:
#       print('Wrong input, try again: ')
#       InputNumber(a, b)

# #Infomation for in put:
# print('Input the product you want to buy: ')  
# for i, j in dict_items.items():
#     print(i, j)
# print('Enter', len(list_items) ,'if you want to stop')
# t = []
# n = InputNumber(0, len(list_items))
# while n!=len(list_items):
#   t.append(n)
#   n = InputNumber(0, len(list_items))
# print("So these are all products you want to buy: ")
# c = []
# for i in range(0, len(t)):
#   b = t[i]
#   print(dict_items[b])
#   c.append(dict_items[b])
# print("Thanks for your buying, here is our suggest for you to select:")
# for i in range(0, len(Suggest(c))):
#   print(Suggest(c)[i], end=', ')
#   if i % 5 == 0 and i > 1:
#     print('\n')