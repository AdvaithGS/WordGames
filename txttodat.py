from pickle import dump
from Classes import Grouper
#import enquiries
#import os
#opt = [i for i in os.listdir() if i.endswith('.txt')]
option = input("Choose option: ")
f = open(option)
l = []

delimiter = input("Enter Delimiter: ")
for i in f:
 l.append(i.strip().split(delimiter))

g = Grouper({},False)
for i in l:
 g.Initiate(i[0])
 for j in i[1:]:
  g.Associate(j,i[0])
print("created groupers")
f = open(option.replace('.txt','.dat'),'wb')
dump(g,f)
f.close()
