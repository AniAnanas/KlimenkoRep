'''Вариант 13.
Дано число R и список размера N. Найти два соседних элемента списка, сумма
которых наиболее близка к числу R, и вывести эти элементы в порядке возрастания
их индексов (определение наиболее близких чисел - то есть такой элемент AK, для
которого величина |AK - R| является минимальной).'''
from random import randint
def typecheck(x, type_:type):
    while type(x) != type_:
        try:
            return type_(x)
        except ValueError:
            x = input(f'Неправильный ввод {"целого " if type_ == int else "вещественного " if type_ == float else ""}числа!\nПовторите ввод: ')
def find_neighbours(R, N):
    min_diff = float('inf')
    min_pair = None
    for i in range(len(N) - 1):
        diff = abs(N[i] + N[i + 1] - R)
        if diff < min_diff:
            min_diff = diff
            min_pair = (N[i], N[i + 1])
    return min_pair
R = randint(1, 100)
N = []
Ns = typecheck(input('Введите размер списка: '), int)
for i in range(Ns):
    N.append(randint(1, 100))
print(f'Число R: {R}\nНайденные соседние элементы:{find_neighbours(R, N)} в списке N:\n{N}')
