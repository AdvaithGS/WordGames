from random import random

class Grouper():
  def __init__(self,d, rigid : bool):
    self.d = d
    self.d1 = {}
    self.rigid = rigid
    
  def Associate(self,x, y):
    ans = None
    for i in self.d:
      for j in self.d[i]:
        if j == x and self.rigid:
          return 
        elif j == y:
          ans = i
    if ans:
      self.d[ans].append(x)
  
  def Initiate(self,y):
    for i in self.d:
      for j in self.d[i]:
        if j == y:
          return 
    key = random()
    while key in self.d:
      key = random()
    self.d[key] = [y]
  
  def GetGroup(self, y , include = True):
    for i in self.d:
      for j in self.d[i]:
        if j == y:
          l = self.d[i]
          if not include:
            l.remove()
          return l
  def __str__(self):
    return str([self.d[i] for i in self.d])
    

    