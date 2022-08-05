
import numpy as np

import pandas as pd

# # Сброс ограничений на количество выводимых рядов
# pd.set_option('display.max_rows', None)
#
# # Сброс ограничений на число столбцов
pd.set_option('display.max_columns', None)
#
# # Сброс ограничений на количество символов в записи
pd.set_option('display.max_colwidth', None)
df = pd.read_csv('temp_1.csv', sep=';')

df['left_bet'] = df['left_bet'].astype(np.uint16)
df['right_bet'] = df['right_bet'].astype(np.uint16)
df['left_ratio'] = df['left_ratio'].astype(np.float16)
df['right_ratio'] = df['right_ratio'].astype(np.float16)
df['left_win'] = df['left_win'].astype(np.int16)
df['right_win'] = df['right_win'].astype(np.int16)
df['sum_win'] = df['left_win'] + df['right_win']
df['diff_win'] = abs(df['left_win'] - df['right_win'])
df = df.loc[df['diff_win'] == df['diff_win'].min()]
# print(df)
print(df.query('ratio == 4.5'))

# print(
#     df.pivot_table(index='ratio', values='sum_win', aggfunc='max').sort_values('sum_win')
# )
