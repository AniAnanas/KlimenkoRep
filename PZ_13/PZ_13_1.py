"""Вариант 13.
1. Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов.
"""
from random import randint

matrixElems = ''
while type(matrixElems) == str:
    try:
        matrixElems = int(input("Введите кол-во элементов в строке матрицы:\n> "))
        if matrixElems <= 0:
            print("Кол-во элементов должно быть больше нуля!")
            matrixElems = ''
    except ValueError: print("Неправильный ввод целого числа")
    except EOFError: print("\r", end="") or exit()
    except KeyboardInterrupt: print("\r", end="") or exit()

matrixRows = ''
while type(matrixRows) == str:
    try:
        matrixRows = int(input("Введите кол-во строк в матрице:\n> "))
        if matrixRows <= 0:
            print("Кол-во элементов должно быть больше нуля!")
            matrixRows = ''
    except ValueError: print("Неправильный ввод целого числа")
    except EOFError: print("\r", end="") or exit()
    except KeyboardInterrupt: print("\r", end="") or exit()
    
matrix = [[randint(-100,100) for elem in range(matrixElems)] for row in range(matrixRows)]

print("\n".join(map(str, matrix)))
stringBuilder = ""
i=1
for line in matrix:
   stringBuilder+=str(i) 