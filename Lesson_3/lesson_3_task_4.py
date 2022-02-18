"""
Определить, какое число в массиве встречается чаще всего.
"""
from random import randint

# формируем список натуральных чисел с повторами
my_numbers = [randint(1, 9) for _ in range(0, 50)]
print(f'Изначальный список:\n{my_numbers}\n')

result = {}

for num in my_numbers:
    if num not in result:
        result[num] = 1
    else:
        result[num] += 1

# сортируем словарь по ключам
# result = dict(sorted(result.items()))

# выводим кол-во вхождений
print('\n'.join([f'Кол-во вхождений {k}: {v}' for k, v in result.items()]))

# выводим результат
# max_index = max(result, key=result.get)

max_count = 0
max_index = 0

for key, value in result.items():
    if value > max_count:
        max_count = value
        max_index = key

print(f'\nПовторы не учитываются\nЧаще всего встречается число {max_index}: {result[max_index]} раз(а)')
