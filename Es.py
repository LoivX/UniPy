##ESERCIZIO##
#importo le librerie necessarie
import math
import random
import statistics

#stampo il fattoriale
print("The factorial of 39 is {} \n".format(math.factorial(39)))

#stampo e
print("Il numero di nepero vale {} \n" .format(math.e))

#definisco le basi 
for b in [math.e, 2, 3, 10]:
    print("Il logaritmo in base {} di e vale {} \n".format(b, math.log(b, 1500)))

#genero un numero casuale nel range [0,1]
print("Un numero casuale nel range [0,1] è {} \n".format(random.random()))

#genero un random float nel range [3.5,13.5]
print("Un numero casuale nel range [3.5,13.5] è {} \n".format(random.uniform(3.5, 13.5)))

#genero numero inter casuale in [5,50]
print("Un numero intero casuale in [5,50] è {} \n".format(random.randint(5, 50)))

#genero un numero pari nell'intervalo [6,60]
print("Un numero pari nell'intervalo [6,60] è {} \n".format(random.randrange(6, 60, 2)))

#calcolo la moda della lista
print("La moda della lista è {} \n".format(statistics.mode([1,1,2,3,3,3,3,4])))

#calcolo la media della lista
print("La media della lista è {} \n".format(statistics.mean([1,2,3,4,5,6,7,8])))