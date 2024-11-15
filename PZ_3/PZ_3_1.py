'''Вариант 13.
    Даны три целых числа: A, B, C. Проверить истинность высказывания: «Хотя бы одно
    из чисел A, B, C положительное».'''
def intcheck(x, n:int):
    while type(x) != int:
        try:
            x = int(x)
            return x
        except ValueError:
            print(f'Неправильно ввели {"первое " if n == 1 else "второе " if n==2 else "третье " if n==3 else ""}число!')
            x = input(f'Введите {"первое " if n == 1 else "второе " if n==2 else "третье " if n==3 else ""}число: ')

a = intcheck(input('Введите первое число: '), 1)
b = intcheck(input('Введите второе число: '), 2)
c = intcheck(input('Введите третье число: '), 3)

print("Одно из чисел положительное" if a>0 or b>0 or c>0 else "Все числа отрицательные")