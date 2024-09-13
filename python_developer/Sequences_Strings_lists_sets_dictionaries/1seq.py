"""
 1) Из всех методов списка (list) выбрать 5 тех, которые по вашему мнению используются чаще всего
 1. append
 2. remove
 3. pop
 4. reverse
 5. sort

 2) Написать их через запятую с параметрами
 1. list.append(x)
 2. list.remove(x)
 3. list.pop([i])
 4. list.reverse()
 5. list.sort(x)

 3). Повторить процедуру для словарей (dict), множеств (set), строк (str)
 dict
 1. dict.items()
 2. dict.get(key[, default])
 3. dict.keys()
 4. dict.values()
 5. dict.update([other])

 set
 1. set.union(other, ...)
 2. set.intersection(other, ...)
 3. set.difference(other, ...)
 4. set.symmetric_difference(other, ...)
 5. set.difference(other, ...)

 str
 1. str.strip([chars])
 2. str.split([chars])
 3. str.upper([chars])
 4. str.find(str, [start],[end])
 5.str.startwith(str)


 Создать новый проект, в нем создать модуль 1seq.py. Задание:
Пользователь вводит количество элементов будущего списка
После этого по очереди по одной вводит любые цифры
Сохранить цифры в список
Отсортировать список по возрастанию и вывести на экран
Пример работы: Введите количество элементов: 3
Введите 1 элемент: 5
Введите 2 элемент: 2
Введите 3 элемент: 4
Вывод: [2, 4, 5]
"""

cnt_elements = int(input(f'Введите количество элементов:'))


list_values=[]
for el in range(cnt_elements):
    list_values.append(int(input(f'Введите {el+1} элемент:')))

list_values.sort()
print(list_values)


