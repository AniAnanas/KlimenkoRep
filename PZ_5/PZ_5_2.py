'''Вариант 13.
    Описать функцию ShiftRight3(A, B, C), выполняющую правый циклический сдвиг:
    значение A переходит в B, значение B в C, значение C в A (A, B, C —
    вещественные параметры, являющиеся одновременно входными и выходными). С
    помощью этой функции выполнить правый циклический сдвиг для двух данных
    наборов из трех чисел: (A1, B1, C1) и (A2, B2, C2).'''

def typecheck(x, type_:type):
    while type(x) != type_:
        try:
            return type_(x)
        except ValueError:
            x = input(f'Неправильный ввод {"целого " if type_ == int else "вещественного " if type_ == float else ""}числа!\nПовторите ввод: ')

def shift_right3(A, B, C):
    return B, C, A

a1 = typecheck(input('Введите число A1: '), float)
b1 = typecheck(input('Введите число B1: '), float)
c1 = typecheck(input('Введите число C1: '), float)
a1, b1, c1 = shift_right3(a1, b1, c1)
print(f"После правого сдвига: A1={a1}, B1={b1}, C1={c1}")

a2 = typecheck(input('Введите число A2: '), float)
b2 = typecheck(input('Введите число B2: '), float)
c2 = typecheck(input('Введите число C2: '), float)
a2, b2, c2 = shift_right3(a2, b2, c2)
print(f"После правого сдвига: A2={a2}, B2={b2}, C2={c2}")