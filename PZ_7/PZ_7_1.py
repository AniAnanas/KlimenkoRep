"""Вариант 13.
1. Дана строка. Подсчитать количество содержащихся в ней цифр."""
f_string = input('Введите строку: ')
f_count = 0
for char in f_string:
    if char.isdecimal():
        f_count += 1
print(f'В введённой строке {f_count} цифр')
