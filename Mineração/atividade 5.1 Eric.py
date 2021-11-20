import numpy as np

valor = int(input('digite o valor: '))

n100 = int(valor/100)
total = valor % 100

n50 = int(valor/50)
total = valor % 50

n10 = int(valor/10)
total = valor%10

n1 = total

print ('Total de notas de 100 = ',n100)
print ('Total de notas de 50 = ',n50)
print ('Total de notas de 10 = ',n10)
print ('Total de notas de 1 = ',n1)