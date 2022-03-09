# uliziando o apriori para validar que qual a frequecia por idade nos tipos de classe
# utilizando o suporte de 1/88 e confiança a 70%

import pandas as pd
from apriori_python import apriori

DataFrame = pd.read_csv('titanic.csv')

grupoSobreviventes = DataFrame.groupby('Age')['Pclass'].apply(list)

freqItensSet, rules = apriori(grupoSobreviventes, minSup = 0.01136, minConf = 0.7)

print(grupoSobreviventes)
print (rules)
