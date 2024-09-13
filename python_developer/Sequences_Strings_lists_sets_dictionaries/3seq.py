"""
Задание:

Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
Затем он вводит элементы 2-го списка
Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
Введите элементы 2-го списка: 2,5
Результат: 1,3,4
"""

first_input = input('Введите элементы 1-го списка:').split(',')
second_input = input('Введите элементы 2-го списка:').split(',')

int_first = [int(num) for num in first_input]
int_second = [int(num) for num in second_input]

for num in int_second:
    if num in int_first:
        counter = int_first.count(num)
        for i_num in range(counter):
            int_first.remove(num)

print(int_first)
