# -*- coding: utf-8 -*-
"""python_week2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Tpr922f043Ef-8Pn1XyEmKcPBiXB09uH
"""

#ex1
num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
k = 3
sub_list = []
for i in range(len(num_list) - k + 1):
    list_1 = num_list[i:i+k]
    sub_list.append(max(list_1))
print(sub_list)

#ex2
word = input("Enter the word: ")
word = word.lower()
dict1 = {}
for i in word:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
print(dict1)

#ex3
!gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko
file_path = '/content/P1_data.txt'
with open(file_path, 'r') as f:
    data = f.read()
    data = data.lower()
    data = data.replace(',', '')
    data = data.replace('.', '')
    data = data.split()
counter = {}
for word in data:
  if word in counter:
    counter[word] += 1
  else:
    counter[word] = 1
print(counter)

#ex4
source = 'yu'
target = 'you'
distance = []
for i in range( len(source) + 1):
  row = [0]*(len(target) + 1)
  distance.append(row)
for i in range(len(source) + 1):
  distance[i][0] = i
for i in range(len(target) + 1):
  distance[0][i] = i
del_cost = 0
ins_cost = 0
sub_cost = 0
for i in range(1, len(source) + 1):
  for j in range(1, len(target) + 1):
      if source[i-1] == target[j-1]:
        distance[i][j] = distance[i-1][j-1]
      else:
        del_cost = distance[i-1][j]
        ins_cost = distance[i][j-1]
        sub_cost = distance[i-1][j-1]
        if del_cost <= ins_cost and del_cost <= sub_cost:
          distance[i][j] = del_cost + 1
        elif ins_cost <= del_cost and ins_cost <= sub_cost:
          distance[i][j] = ins_cost + 1
        else:
          distance[i][j] = sub_cost + 1
levenstein_distance = distance[-1][-1]
print (levenstein_distance)