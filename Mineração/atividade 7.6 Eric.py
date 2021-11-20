import numpy as np

x = int(input('digite um numero: '))

y = []

for i in range(x):
    y.append(i) 

print(y)

soma = sum(y)
print('soma: ',soma)

media = len(y)
print('media: ',media)

maior =  max(y)
print('maior: ',maior)

menor = min(y)
print('menor: ',menor)