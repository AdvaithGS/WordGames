from random import choice
import enquiries
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

    option = enquiries.choose(ques,opt)
    
    print(ques)

    if option == ans:
        print(colored('Correct! ','green'))
    else:
        print(colored(f'Wrong, correct answer is {ans}\n', 'red'))
    