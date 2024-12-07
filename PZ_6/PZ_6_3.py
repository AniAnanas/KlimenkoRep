'''Вариант 13.
Дан список размера N и целое число K (1 < K < N). Осуществить сдвиг элементов списка влево на K позиций (при этом AN перейдет в AN-K, AN-1 — в AN-K-1, ..AK+1 — в A1, а исходное значение K первых элементов будет потеряно). Последние K элементов полученного списка положить равными 0.'''
from random import randint
def typecheck(x, type_:type):
    while type(x) != type_:
        try:
            return type_(x)
        except ValueError:
            x = input(f'Неправильный ввод {"целого " if type_ == int else "вещественного " if type_ == float else ""}числа!\nПовторите ввод: ')
def shift_left(lst, K):
    # Сдвигаем элементы влево на K позиций
    new_lst = lst[K:] + [0] * K
    return new_lst
N = typecheck(input("Введите размер списка: "), int)
K = typecheck(input("Введите количество позиций для сдвига: "), int)
A = []
while K < N:
    print('Число K должно быть больше N.')
    N = typecheck(input("Введите размер списка: "), int)
    K = typecheck(input("Введите количество позиций для сдвига: "), int)
for i in range(N):
    A.append(randint(0, 100))
print("Исходный список:", A)
print("Сдвинутый список:", shift_left(A, K))
