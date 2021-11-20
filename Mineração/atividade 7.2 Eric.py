nomes = []
nome = input('digite um nome: ')

while nome != '':
    nome = input('digite um nome: ')
    nomes.append(nome)

for i in nomes:
        X = {'nome':i, 'quantidade':nomes.count(i)}
        print(X)

