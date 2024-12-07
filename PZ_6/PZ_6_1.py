'''Вариант 13.
Дан список A размера N. Вывести вначале его элементы с четными номерами (в
порядке возрастания номеров), а затем — элементы с нечетными номерами (также в
порядке возрастания номеров): A2, A4, А6, . . ., A1, A3, A5, ... . Условный оператор не
использовать.'''
from random import randint
def typecheck(x, type_:type):
    while type(x) != type_:
        try:
            return type_(x)
        except ValueError:
            x = input(f'Неправильный ввод {"целого " if type_ == int else "вещественного " if type_ == float else ""}числа!\nПовторите ввод: ')
a, odd, even = [], [], []
n = typecheck(input("Введите размер списка: "), int)
for i in range(n):
    a.append(randint(-100, 100))
for i in range(0,len(a),2):
    even.append(a[i])
for i in range(1,len(a),2):
    odd.append(a[i])
print(f'Полученный список:{a}\nСписок с четными индексами:{even}\nСписок с нечётными индексами:{odd}')