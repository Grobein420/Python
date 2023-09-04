# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 20:48:42 2023

@author: Tobi
"""

def conv_température(unité,température):
    

    if unité==("Cel"):
        température=(température*1.8)+32
        print("La température est de",température,"degrés Fahrenheit")
    elif unité==("Fahr"):
        température=(température-32)/1.8
        print("La température est de",température,"degrés Celsius")
    


    
    
      
    
