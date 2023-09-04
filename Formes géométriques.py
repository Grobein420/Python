# -*- coding: utf-8 -*-
"""
Created on Fri Sep  1 14:10:13 2023

@author: Tobi
"""

import turtle
import math
import tkinter as tk
turtle.reset
écran=turtle.Screen
turtle.setup(640,640,0,0)


def étoile():
    for i in range(5):
        turtle.forward(180)
        turtle.left(180-(180/5))
        
                        

def carré():
    for i in range(4):
        turtle.forward(180)
        turtle.left(90)

def triangle():
    for i in range(3):
        turtle.forward(180)
        turtle.left(120)
        

def rectangle():
    for i in range(2):
        turtle.forward(180)
        turtle.left(90)
        turtle.forward(120)
        turtle.left(90)
        
def cercle():
    for i in range(360):
        turtle.forward(1)
        turtle.left(1)
        


appli=tk.Tk()
appli.title=("Formes géométiques")

démarrage=tk.Label(appli, text=("Quel figure veux-tu que je réalise?:"))
démarrage.pack()

bouton_étoile=tk.Button(appli, text=("Etoile"), command=étoile)
bouton_étoile.pack()

bouton_carré=tk.Button(appli, text=("Carré"), command=carré)
bouton_carré.pack()

bouton_triangle=tk.Button(appli, text=("Triangle"), command=triangle)
bouton_triangle.pack()

bouton_rectangle=tk.Button(appli, text=("Rectangle"), command=rectangle)
bouton_rectangle.pack()

bouton_cercle=tk.Button(appli, text=("Cercle"), command=cercle)
bouton_cercle.pack()

bouton_effacer=tk.Button(appli, text=("Effacer"), command=turtle.reset)
bouton_effacer.pack()
appli.mainloop()

        
print()

turtle.exitonclick()    
                                