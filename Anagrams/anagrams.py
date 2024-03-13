from Classes import Grouper
from pickle import load
from termcolor import colored
from random import shuffle
f = open('anagrams.dat','rb')
g : Grouper = load(f)
f.close()


for n in range(1, int(input("Rounds: ")) + 1):
 rw = g.RandomWord()
 l = g.GetGroup(rw,False)
 correct = 0
 total = len(l)
 color = 'white'
 x = ''
 while l:
  print(colored(f'{n}. ' + rw + f" ({correct}/{total})",color),end = ': ')
  x = input()
  try:
   l.remove(x)
   correct += 1
   color = 'green'
  except:
   if(x != '.s'):
    color = 'red'
  if x == '.q':
    for i in l:
     print(i,end = ' ')
    print()
    break
  elif x == '.s':
    rw = list(rw)
    shuffle(rw)
    rw = ''.join(rw)
 else:
  print(colored(f'{n}. ' + rw + f" ({correct}/{total})",'green'))