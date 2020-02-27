import numpy as np
import pandas as pd
print('--- Dados ausentes ---')
print()

print('1. Criando Datafram com base em dicionario')
d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan],
 'C': [1, 2, 3]}
print(d)
print()

print('2. Simulando um dataframe com dados ausentes')
df = pd.DataFrame(d)
print(df)
print()

print('3. Dropando dados nan - df.dropna')
# df.dropna(axis=0, inplace=True)
# parametro tresh define a qtd de valores nan que devem ter para ser excluido
print(df.dropna(axis=0))
print()

print('4. Substitui dados nan - df.filna')
# Parametro inplace=True para substituir no proprio dataframe
print(df.fillna(value='oi'))
print()

print('5. Preenche valores nan com base na media da coluna A')
# Parametro inplace=True para substituir no proprio dataframe
print(df['A'].fillna(value=df['A'].mean(), inplace=True))
print(df)
print()

print('6. Preenche valores nan com os próximos valores')
df = pd.DataFrame(d)
df.fillna(method='ffill', inplace=True)
print(df)
print()

print()
