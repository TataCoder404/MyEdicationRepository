'''
# 1
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

'''
'''
# 2
import re

reviews = [
"Этот товар просто потрясающий! Очень нравится качество.",
"Неплохо, но могло бы быть и лучше. Цена слишком высокая за то, что вы получаете.",
"Просто ужасно. Сломался через 2 дня использования. Деньги на ветер!!!",
"Хороший товар, быстрая доставка, покупкой доволен.",
"В лучшем случае посредственно. Ничего особенного, но и не ужасно."
]

# 1)	Приведите весь текст к нижнему регистру и удалите пунктуацию
text = " ".join(reviews)
clean_text = re.sub(r"[^\w\s]", "", text, flags=re.UNICODE)
low_clean_text = clean_text.lower()

# 2)	Составьте список всех слов и посчитайте частоту каждого слова
new_list = []
f_words = {}

new_list = low_clean_text.split()

for i in new_list:
    count = 0
    for j in new_list:
        if i == j:
            count += 1
        else:
            continue
    f_words[i]=count
    count = 0

# 3)	Найдите пять самых частых слов
sorted_f_words = []

sorted_f_words = sorted(f_words.items(), key=lambda x: x[1], reverse=True)
top5 = sorted_f_words[:5]
print(f'Пять самых частых слов:\n{top5}')

# Способ получить пять самых частых слов без предварительной сортировки
import heapq
print(heapq.nlargest(5, f_words.items(), key=lambda x: x[1]))

'''

# 3

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