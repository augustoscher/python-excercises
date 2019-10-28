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