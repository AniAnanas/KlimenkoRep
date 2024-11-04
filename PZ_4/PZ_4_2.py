'''Вариант 13.
    Дано целое число N (> 1). Вывести наименьшее из целых чисел K, для которых
    сумма 1 + 2 + . . . + K будет больше или равна N, и саму эту сумму.'''

def typecheck(x, type_:type):
    while type(x) != type_:
        try:
            return type_(x)
        except ValueError:
            x = input(f'Неправильный ввод {"целого " if type_ == int else "вещественного " if type_ == float else ""}числа!\nПовторите ввод: ')

n = input('Введите целое число: ')
n = typecheck(n, int)
k = 0
sum = 0

while sum < n:
    k += 1
    sum += k

print(f'Минимальная K: {k}\nСумма чисел: {sum}')