import numpy as np
import pandas as pd
print('--- Dataframes Multilevel index ---')

print('1. Niveis de indice')
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]

# Cria uma lista de tuplas associando os valores outside com inside
hier_index = list(zip(outside, inside))
print(hier_index)
print()

# Cria objeto do pandas de indice multinivel
hier_index = pd.MultiIndex.from_tuples(hier_index)

print('2. Criando dataframe com indice multinivel')
df = pd.DataFrame(np.random.randn(6, 2), index=hier_index, columns=['A', 'B'])
print(df)
print()

print('3. Acessando dataframes multiniveis')
print(df.loc['G1'])
print()
# Retorna um dataframe, que depois do .loc retorna a serie
print(df.loc['G1'].loc[1])
print()

print('4. Definindo nomes para os indices')
df.index.names = ['Grupo', 'Item']
print(df)
print()

print('5. Selecionando valores conforme level')
print(df.xs(1, level='Item'))
print()
