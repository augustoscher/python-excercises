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

# Buscar valores do dataframe
# 1- Linha/Coluna
print(df.loc['A', 'W'])
print()

# 2- Somente uma linha. Retorna uma serie
print(df.loc['A'])
print()

# 3- Passando listas de linhas e colunas
r = df.loc[['A','C'], ['X', 'Z']]
print(type(r))
print(r)
print()

# Seleciona dados usando notação de indices de numpy
# Linha/Coluna
r = df.iloc[1:4, 2:]
print(type(r))
print(r)
print()






