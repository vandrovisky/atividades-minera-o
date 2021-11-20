menu = int(input(' 1= soma \n 2= sub \n 3= mult \n 4= div \n digite uma das opcoes: '))

if(menu == 1):
    v1 = int(input('digite o valor 1: '))
    v2 = int(input('digite o valor 2: '))

    soma = v1+v2
    print('soma: ',soma)

elif(menu == 2):
    v1 = int(input('digite o valor 1: '))
    v2 = int(input('digite o valor 2: '))

    sub = v1-v2
    print('sub: ',sub)

elif(menu == 3):
    v1 = int(input('digite o valor 1: '))
    v2 = int(input('digite o valor 2: '))

    mult = v1*v2
    print('mult: ',mult)

elif(menu == 4):
    v1 = int(input('digite o valor 1: '))
    v2 = int(input('digite o valor 2: '))

    div = v1/v2
    print('div: ',div)

else: 
    print('opcao nao disponivel')    