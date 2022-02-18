"""
В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""
from random import sample

# формируем список
my_numbers = sample(range(-100, 100), 20)
print(f'Изначальный список:\n{my_numbers}')

# выделяем все отрицательные числа, запоминая индексы в виде ключей
my_negative_numbers = {i: num for i, num in enumerate(my_numbers) if num < 0}
print(f'Словарь всех отрицательных чисел из основного списка (ключи - индексы):\n{my_negative_numbers}')

max_negative_index = 0
max_negative_number = -100

for key, value in my_negative_numbers.items():
    if value > max_negative_number:
        max_negative_number = value
        max_negative_index = key

print(f'Максимальное отрицательное число: {max_negative_number}\nИндекс в основном массиве: {max_negative_index}')
