# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 20:48:42 2023

@author: Tobi
"""
import tkinter as tk

appli=tk.Tk()
appli.title=("Convertisseur")

démarrage=tk.Label(appli, text=("Bienvenue sur le convertisseur:"))
démarrage.pack()

celsius_label=tk.Label(appli, text=("Celsius:"))
celsius_label.pack()

celsius_entry=tk.Entry(appli)
celsius_entry.pack()

fahrenheit_label=tk.Label(appli, text=("Fahrenheit:"))
fahrenheit_label.pack()

fahrenheit_entry=tk.Entry(appli)
fahrenheit_entry.pack()


def conv_température():
    try:
        celsius=float(celsius_entry.get())
        fahrenheit=(celsius*9/5)+32
        fahrenheit_entry.delete(0, tk.END)
        fahrenheit_entry.insert(0, fahrenheit)
    except ValueError:
        fahrenheit_entry.delete(0, tk.END)
        fahrenheit_entry.insert(0, "Donnée invalide, veuillez réssayer")
        
bouton_convertir=tk.Button(appli, text=("Convertir:"), command=conv_température)
bouton_convertir.pack()


appli.mainloop()



    
    
      
    
