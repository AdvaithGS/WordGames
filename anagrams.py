from Classes import Grouper
from pickle import dump

g = Grouper({},True)
with open('anagrams.txt') as f:
 for i in f:
  x = i.strip().split()
  g.Initiate(x[0])
  for i in range(1,len(x)):
   g.Associate(x[i],x[0])


f = open('anagrams.dat','wb')
dump(g,f)

