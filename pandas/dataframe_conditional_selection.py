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

print('4. Condicional com multiplas condições')
# Precisa usar o operador & em vez de and
# and não esta preparado para comparar series
ret = df[(df['W'] > 0) & (df['Y'] > 1)]
print(ret)
print()


print('5. ')
print()