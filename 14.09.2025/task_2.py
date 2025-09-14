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
# import heapq
# print(heapq.nlargest(5, f_words.items(), key=lambda x: x[1]))