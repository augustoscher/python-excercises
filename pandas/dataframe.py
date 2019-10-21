import numpy as np
import pandas as pd
print('--- Pandas/Dataframes ---')

np.random.seed(101)

df = pd.DataFrame(np.random.randn(5, 4), 'A B C D E'.split(), 'W X Y Z'.split())
print(df)
print()

# Consumo de dados de um Dataframe
