'''Вариант 13.
    Даны три целых числа: A, B, C. Проверить истинность высказывания: «Хотя бы одно
    из чисел A, B, C положительное».'''
def intcheck(x, n):
    while type(x) != int:
        try:
            x = int(x)
            return x
        except:
            print(f'Неправильно ввели {"первое" if n == 1 else "второе" if n==2 else "третье"} число!')
            x = input(f'Введите {"первое" if n == 1 else "второе" if n==2 else "третье"} число: ')
a, b, c = input('Введите первое число: '), input('Введите второе число: '), input('Введите третье число: ')
a, b, c = intcheck(a, 1), intcheck(b, 2), intcheck(c, 3)
print("Одно из чисел положительное" if a>0 or b>0 or c>0 else "Все числа отрицательные")