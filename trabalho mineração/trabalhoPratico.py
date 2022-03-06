import pandas as pd
from apriori_python import apriori

campeoes = pd.read_csv('dataset_champions.csv')

grupo_attackdamage = campeoes.groupby('attackdamage')['tags'].apply(list)
grupo_attackspeed = campeoes.groupby('attackspeed')['tags'].apply(list)
grupo_armor = campeoes.groupby('armor')['tags'].apply(list)

freqItensSet1, rules1 = apriori(grupo_attackdamage, minSup = 0.1, minConf = 0.9)
freqItensSet2, rules2 = apriori(grupo_attackspeed, minSup = 0.09, minConf = 0.9)
freqItensSet3, rules3 = apriori(grupo_armor, minSup = 0.1, minConf = 0.9)

print(f'----------------------------------------------------------')
print(grupo_attackdamage)
print(rules1)
print(f'----------------------------------------------------------')
print(grupo_attackspeed)
print(rules2)
print(f'----------------------------------------------------------')
print(grupo_armor)
print(rules3)