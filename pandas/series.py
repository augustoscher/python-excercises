import numpy as np
import pandas as pd
print('--- Pandas/Series ---')

labels = ['a', 'b', 'c']
values = [10, 20, 30]
array = np.array([10, 20, 30])
dic = {'a': 10, 'b': 20, 'c': 30} 

# Transformando dados normais em séries
print('Gerando series com base em uma lista')
s1 = pd.Series(data=values, index=labels)
print(s1)
print()

print('Gerando series com base em um np.array')
s2 = pd.Series(array, labels)
print(s2)
print()

print('Gerando series com base em dicionario')
s3 = pd.Series(dic, dic.keys())
print(s3)
print()


# Operações com indices
ser1 = pd.Series([1, 2, 3, 4, 5, 6], index=['EUA', 'Alemanha', 'Inglaterra', 'Rússia', 'Japão', 'China'])
ser2 = pd.Series([1, 2, 3, 4, 5, 6], index=['EUA', 'Alemanha', 'Inglaterra', 'Brasil', 'Japão', 'China'])
print(ser1)
print()
print(ser2)
print()
ser3 = ser1 + ser2
print(ser3)
