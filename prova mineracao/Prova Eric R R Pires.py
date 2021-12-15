import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('titanic.csv')

print(titanic.head(10)) # parte referente a letra a)

titanic = titanic.sort_values('Name') # parte referente a letra b)

print(titanic)

titanic = titanic.assign(Sobrevivente = '') # parte referente a letra c)
titanic.loc[titanic.Survived == 0, 'Sobrevivente']='Nao'
titanic.loc[titanic.Survived == 1, 'Sobrevivente']='Sim'

print(titanic.head(10))

titanic = titanic.drop(columns=['SibSp','Parch','Ticket'])# parte referente a letra d)

print(titanic.head(10))

titanic =  titanic.rename(columns={'PassengerId': 'PassageiroID'})# parte referente a letra e)
titanic =  titanic.rename(columns={'Survived': 'Sobreviveu'})
titanic =  titanic.rename(columns={'Pclass': 'Pclasse'})
titanic =  titanic.rename(columns={'Name': 'Nome'})
titanic =  titanic.rename(columns={'Sex': 'Sexo'})
titanic =  titanic.rename(columns={'Age': 'Idade'})
titanic =  titanic.rename(columns={'Fare': 'tarifa'})
titanic =  titanic.rename(columns={'Cabin': 'Cabine'})
titanic =  titanic.rename(columns={'Embarked': 'Embarcado'})

print(titanic.head(10))

titanic.loc[titanic.Sexo == 'male', 'Sexo']='masculino' # parte referente a letra f)
titanic.loc[titanic.Sexo == 'female', 'Sexo']='FEMININO'

print(titanic.head(10))

sobreviventePorClasse = titanic.groupby(['Pclasse','Sobreviveu']).count()# parte referente a letra g)

print(sobreviventePorClasse)

mortosPoreSexo = titanic.groupby(['Sexo','Sobreviveu']).count()# parte referente a letra h)

print(mortosPoreSexo)


plt.bar(titanic['Pclasse'], titanic['Sobreviveu'])
plt.show()

titanic.to_excel('titanic Eric.xlsx')