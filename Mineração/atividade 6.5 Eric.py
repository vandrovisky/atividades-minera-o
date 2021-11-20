n = int(input('digite o valor a ser fatorado: '))

def fatorial(n):
    fat = 1

    for i in range(1, n+1):
        fat = fat*i
    
    return(fat)

print(fatorial(n))

