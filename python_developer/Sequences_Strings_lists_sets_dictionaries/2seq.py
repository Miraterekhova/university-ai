"""создать модуль 2seq.py. Задание:
Пользователь вводит любые цифры через запятую
Сохранить цифры в список
Получить новый список в котором будут только уникальные элементы исходного (уникальным считается символ, который встречается в исходном списке только 1 раз)
Вывести новый список на экран
Порядок цифр в новом списке не важен
Пример работы: Введите элементы списка через запятую: 2,3,4,5,5,6,5,3,9
Результат: 2, 4, 6, 9
(Дополнительно*)
Предусмотреть что пользователь может использовать один из 3-х разделителей:
запятую, точку с запятой, слэш (1,2,3 1;2;3 1/2/3), но только какой то один 1,2;3/4 - так нельзя
"""


input_str = input('Введите элементы списка через запятую:')
if ',' in input_str:
        separator = ','
elif ';' in input_str:
    separator = ';'
elif '/' in input_str:
    separator = '/'
else:
    raise ValueError("Неверный разделитель. Используйте ',', ';' или '/'.")


num_list = [int(num) for num in input_str.split(separator)]

print(set(num_list))