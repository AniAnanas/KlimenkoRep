'''Вариант 13.
    Дано вещественное число A и целое число N (>0). Найти A в степени N: AN = AA ...
    •A (числа A перемножаются N раз).'''

def typecheck(x, type_:type):
    while type(x) != type_:
        try:
            return type_(x)
        except ValueError:
            x = input(f'Неправильный ввод {"целого " if type_ == int else "вещественного " if type_ == float else ""}числа!\nПовторите ввод: ')

a = typecheck(input('Введите вещественное число: '), float)
n = typecheck(input('Введите целое число: '), int)
b = a

for i in range(n-1):
    a *= b

print(a)