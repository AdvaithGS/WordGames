git remote add origin https://github.com/AdvaithGS/WordGames.git
  git branch -M main
  git push -u origin mainfrom random import random
d = {}

class Grouper(str):
 def __init__(self, name : str, d :dict):
  self.name = name
  self.d = d
 
 def ParentGroup(self):
  return self.d[self.Group_Id]
 
 def Initiate(self):
  Group_Id = random.random()
  while Group_Id in self.d:
   Group_Id = random.random()
  self.Group_Id = Group_Id
  d[self.Group_Id] = [self.name]
 
 def __str__(self):
  return self.name

 def Associate(self, x : Grouper):
  self.Group_Id = x.Group_Id
  d[self.Group_Id].append(self.name)

