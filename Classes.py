from random import random,choice,sample

class Grouper():
  def __init__(self,d, rigid : bool):
    self.d = d
    self.rigid = rigid
    
  def Associate(self,new, old):
    ans = None
    for i in self.d:
      for j in self.d[i]:
        if j == new and self.rigid:
          return 
        elif j == old:
          ans = i
    if ans:
      self.d[ans].append(new)
  
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
            l.remove(y)
          return l
  def RandomWord(self, z = 1):
    if z == 1:
      return choice(self.d[choice(list(self.d.keys()))])
    elif z > 1:
      l = []
      for i in sample(list(self.d.keys()),k = z):
        l.append(choice(self.d[i]))
      return l
  def __str__(self):
    return str([self.d[i] for i in self.d])  

    