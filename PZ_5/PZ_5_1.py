'''Вариант 13.
    Найти сумму чисел ряда 1,2,3,...,60 с использованием функции нахождения суммы.
    Использовать локальные переменные.'''

def typecheck(x, type_:type):
    while type(x) != type_:
        try:
            return type_(x)
        except ValueError:
            x = input(f'Неправильный ввод {"целого " if type_ == int else "вещественного " if type_ == float else ""}числа!\nПовторите ввод: ')

def sum_range(n, m):
    total = 0
    for i in range(n, m + 1):
        total += i
    return total

n = typecheck(input("Введите начальное число n: "), int)
m = typecheck(input("Введите конечное число m: "), int)

print(f"Сумма чисел от {n} до {m} равна: {sum_range(n,m)}")