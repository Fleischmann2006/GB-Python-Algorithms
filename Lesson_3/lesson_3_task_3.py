"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""
from random import sample

# создаём список из 10-ти уникальных случайных чисел от 1 до 99
my_numbers = sample(range(1, 100), 10)
print(f'Изначальный список:\n{my_numbers}')

min_num_index, max_num_index = 0, 0

# находим индекс наименьшего и наибольшего чисел из списка за 1 проход
for i, num in enumerate(my_numbers):
    if num > my_numbers[max_num_index]:
        max_num_index = i
    if num < my_numbers[min_num_index]:
        min_num_index = i

# выводим наименьшее и наибольшее числа
print(f'\nНаименьшее число: {my_numbers[min_num_index]}\nНаибольшее число: {my_numbers[max_num_index]}')

# меняем числа местами, зная индексы
my_numbers[min_num_index], my_numbers[max_num_index] = my_numbers[max_num_index], my_numbers[min_num_index]

# выводим результат
print(f'\nПосле перестановки:\n{my_numbers}')
