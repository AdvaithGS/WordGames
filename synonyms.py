from random import choice
from termcolor import colored 
from Classes import Grouper
from pickle import load

f = open("synonyms.dat",'rb')
g : Grouper = load(f)

for j in range(3):    
    opt = g.RandomWord(4)
    
    grp  = g.GetGroup(ans := choice(opt))
    grp.remove(ans)
    ques = choice(grp)       
    print(ques)
    for index, o in enumerate(opt):
        print(f"{index + 1}. {opt[index]}")
    option = {index+1:o for index,o in enumerate(opt)}[int(input("Choose: "))]
    
    if option == ans:
        print(colored('\nCorrect! \n','green'))
    else:
        print(colored(f'Wrong, correct answer is {ans}\n', 'red'))
    