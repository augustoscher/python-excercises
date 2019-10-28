import numpy as np
import pandas as pd
print('--- Pandas/Dataframes ---')

np.random.seed(101)

df = pd.DataFrame(np.random.randn(5, 4), index='A B C D E'.split(), columns='W X Y Z'.split())
print(df)
print()

# Consumo/indexação de dados de um Dataframe

# Busca os dados da coluna "W". Irá retornar uma serie
s1 = df['W']
print(type(s1))
print(s1)
print()

# É possível passar uma lista de colunas. Retorna um outro dataframe
s2 = df[['W', 'Z']]
print(type(s2))
print(s2)
print()

# Criando uma nova coluna no dataframe
df['NEW'] = df['X'] + df['Y']
print(df)
print()

# Deletar coluna no eixo 1 (colunas) 
df.drop('NEW', axis=1, inplace=True)
# ou
# df = fd.drop('NEW', axis=1, inplace=True)
print(df)
print()