import pandas as pd

df = pd.read_csv('data_1.csv')
print(df)

df_filtr = df[(df['value'] >= 0) & (df['value'] <= 100)]

s_avg = df_filtr.groupby('sensor_id')['value'].mean()
df_avg = s_avg.reset_index()
df_avg.columns = ['sensor_id', 'value']
print(f'Средние значения показаний для датчиков:\n{df_avg}\n')

avg_max = s_avg.idxmax()
print(f'Датчик с максимальным средним значением:\n{avg_max}')