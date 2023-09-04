
"""
Created on Thu Aug 31 16:45:33 2023

@author: Tobi
"""
a=int(input("Quel est le plus petit nombre ?"))
b=int(input("Quel est le plus grand nombre ?"))
n=0
A=a
x=int(input("Quel est le multiple?"))
for k in range(a,b+1):
    if A%x==0:
        n=n+1
    A=A+1

print("Entre",b," et ",a," il y a",n,"multiple de",x,)
print(b,"et",a,"compris")

