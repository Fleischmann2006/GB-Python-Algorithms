"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
Примечание: 8 разных ответов.
"""

my_numbers = list(range(2, 100))
print('Список натуральных чисел от 2 до 99 (включительно):')
print(my_numbers)

my_divs = list(range(2, 10))
print('Список делителей (натуральные числа от 2 до 9):')
print(my_divs)

result = {key: [] for key in my_divs}

for num in my_numbers:
    for div in my_divs:
        if num % div == 0:
            result[div].append(num)

print('\n'.join([f'На {k} без остатка делится {len(v)} чисел: {v}' for k, v in result.items()]))
