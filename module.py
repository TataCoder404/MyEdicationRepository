# 1.	Напишите функцию days_until_new_year, которая возвращает количество дней до ближайшего Нового Года.

# from datetime import date

# dt = date.today()
# dt_new_year = date(year=2025, month = 12, day=31)

# delta = dt_new_year - dt
# print(type(delta))
# print(delta.days)
# print(type(delta.days))


# 2.	Напишите функцию, которая принимает диаметр пиццы в см и возвращает площадь в см² округленную до целого.

# import math

# def pizza(r):
#     S = round(math.pi * math.pow(r, 2), 2)
#     print(f'Плащадь пиццы: {S} см²')

# pizza(3)

# 3.	Создайте функцию workday_count(start_date, end_date) которая считает количество рабочих дней (пн-пт) между двумя датами включительно.
#       Формат дат: 'DD-MM-YYYY'

# from datetime import datetime, timedelta


# def workday_count(start_date, end_date):
#     start_dt = datetime.strptime(start_date, '%d-%m-%Y')
#     end_dt = datetime.strptime(end_date, '%d-%m-%Y')
#     count = 0
#     current_dt = start_dt
    
#     while current_dt <= end_dt:
#         if current_dt.weekday() < 5:  # 0-4 это понедельник-пятница
#             count += 1
#         current_dt += timedelta(days=1)

#     return count

# print(workday_count('10-07-2025', '10-08-2025'))


# 4.	Используя datetime посчитайте точное время до полуночи в формате HH:MM:SS.

# from datetime import date, datetime, timedelta

# dt = datetime.today()

# delta = timedelta(days=1)

# midnight = dt + delta
# midnight = midnight.replace(hour=0, minute=0, second=0, microsecond=0)


# before_midnight = midnight - dt

# print(before_midnight)



