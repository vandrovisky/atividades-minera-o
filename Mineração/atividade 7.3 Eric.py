frase = str(input('Digite uma frase: ')) 
F = frase.split()

for i in F:
    if i.islower() != True and i.isalpha() == True:
        frase = frase.replace(i,"********")

print(frase)