import pandas as pd

df = pd.read_csv('data_3.csv')

# 1)	Рассчитайте общий итоговый баланс.

total = df["value"].sum()
print(f'Общий итоговый баланс:\n{round(total,2)}\n')

# 2)	Найдите самую крупную трату и самый большой доход

import heapq

largest_spend = heapq.nsmallest(1,df["value"])
largest_income = heapq.nlargest(1,df["value"])

print(f'Самая крупная трата:\n{float(largest_spend[0])}\n\nСамый большой доход:\n{float(largest_income[0])}\n')

# 3)	Создайте отчет об изменении баланса по неделям

df["date"] = pd.to_datetime(df["date"])
df["week_number"] = df["date"].dt.isocalendar().week

df_pivot = df.pivot_table(values='value', index='week_number', aggfunc='sum')

print(f'Отчёт в разрезе недель:\n{df_pivot}')