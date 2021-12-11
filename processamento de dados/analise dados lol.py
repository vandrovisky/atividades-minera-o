import pandas as pd
import matplotlib.pyplot as plt

champions = pd.read_csv("dataset_champions.csv")

print(champions.count())

champions.drop(champions.loc[champions['tags'] == ''].index, inplace= True) #eliminando todos os champs sem tags definidas

groupMarksman = champions.loc[champions['tags'] == "['Marksman']"] # selecioando todos os atiradores
groupTank = champions.loc[champions['tags'] == "['Tank']"] # selecioando todos os tanques
groupMage = champions.loc[champions['tags'] == "['Mage']"] # selecioando todos os magos

plt.bar(groupMarksman['id'],groupMarksman['attack'])
plt.title('atirador com mais ataque')
plt.ylabel('ataque base')
plt.xlabel('campeoes')
plt.show()

plt.scatter(groupTank['id'],groupTank['hpperlevel'])
plt.title('tank com mais hp por lvl')
plt.ylabel('HP por lvl')
plt.xlabel('campeoes')
plt.show()

barra1 = plt.bar(groupMage['id'],groupMage['mp'])
barra2 = plt.bar(groupMage['id'],groupMage['mpperlevel'])
plt.bar_label(barra1, label_type='center')
plt.bar_label(barra2, label_type='center')
plt.title('Magos com maior mana e mana por level')
plt.ylabel('mana + mana por lvl')
plt.xlabel('campeoes')
plt.show()



