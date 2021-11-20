n = int(input('digite um numero: '))

print ('os '+ str(n) +' primeiros numeros da sequencia fibonacci: ' )

prox = 0
ant = 0

while(prox < n):
    print(prox)
    prox = prox + ant
    ant = prox - ant

    if(prox == 0):
        prox =+ 1