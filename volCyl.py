##ESERCIZIO##
#importo le librerie
import numpy

#Definisco una funzione che calcola il volume di un cilindro
def volCyl(r=1, h=1):
    return np.pi * r**2 * h

#definisco una funzione che stampa 'Hello World'
def printHelloWorld():
    print("Hello World")

"""
======================================================================
    Main
======================================================================
"""
print(volCyl(3,6))
printHelloWorld()