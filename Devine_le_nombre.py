# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 18:02:41 2023

@author: Tobi
""" 
"""
Bienvenue sur "Guess the number".Essayez de deviner le nombre auquel
je pense selon les limites que vous m'imposez.
Bonne chance :)
"""
import random

number=0
d=int(input("La limite la plus petite est ?"))
f=int(input("La plus grande est ?"))

number=random.randint(d,f)  
                     
answer=int(input("A quel nombre est-ce que je pense?"))
                 
if number==answer:
    print("Bravo tu as trouvé, le nombre était bien",number)
else:
    print("Désolé tu as perdu, le bon nombre était",number)    
    
    