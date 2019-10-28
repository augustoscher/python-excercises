import numpy as np
import pandas as pd
print('--- Dataframes Conditional Selection ---')

np.random.seed(101)

df = pd.DataFrame(np.random.randn(5, 4), index='A B C D E'.split(), columns='W X Y Z'.split())
print(df)
print()


print('1. Condicional com array de boolean')
ret = df > 0
print(ret)
print(df[ret])
print()

print('2. Condicional em séries específicas')
ret = df[df['W'] > 0]
print(ret)
print()

print('3. Condicional em séries específicas com slice')
# retorna os valores da coluna y aos quais os valores de W > 0
print(df[df['W'] > 0]['Y'])
print()

print('4. Condicional com multiplas condições AND')
# Precisa usar o operador & em vez de and
# and não esta preparado para comparar series
ret = df[(df['W'] > 0) & (df['Y'] > 1)]
print(ret)
print()


print('5. Condicional com multiplas condições OR')
# Precisa usar o operador | em vez de or
# or não esta preparado para comparar series
ret = df[(df['W'] > 0) | (df['Y'] > 1)]
print(ret)
print()

print('6. Reset index')
# Remove o indice definido na construção do dataframe
# Adiciona uma coluna chamada 'index' que vira o indice padrão
df.reset_index(inplace=True)
print(df)
# ou
# df = df.reset_index()
print()

print('7. Reset index passing index')
col = 'RS SC PR SP RJ'.split()
df['STATE'] = col
print(df)
print()

df.set_index('STATE', inplace=True)
print(df)
print()