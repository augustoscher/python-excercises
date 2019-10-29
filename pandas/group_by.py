import numpy as np
import pandas as pd
print('--- GroupBy ---')
print()

print('1. Criando Datafram com base em dicionario')
data = {'Empresa': ['GOOG', 'GOOG', 'MSFT', 'MSFT', 'FB', 'FB'],
'Nome':['Sam', 'Charlie', 'Any', 'Vanessa', 'Carl', 'Sarah'],
'Venda':[200, 120, 340, 124, 243, 350]}
print(data)
print()

df = pd.DataFrame(data)
print(df)
print()

print('2. Agrupando dados de dataframe com groupBy - Empresa')
groupEmpresa = df.groupby('Empresa')
print('Soma de vendas por empresa:')
print(groupEmpresa.sum())
print()
print('Média de vendas por empresa:')
print(groupEmpresa.mean())
print()
print('Describe:')
print(groupEmpresa.describe())
print()

print('3. Agrupando dados de dataframe com groupBy - Nome')
groupNome = df.groupby('Nome')
print('Soma de vendas por Nome:')
print(groupNome.sum())
print()
print('Vendas da Any:')
print(groupNome.sum().loc['Any'])
print()

