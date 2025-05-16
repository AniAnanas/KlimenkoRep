"""Вариант 13.
1. Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов.
"""
from random import randint
maxNum = 20
min_range = -100
max_range = 100

def cexit():
    print("\r", end="")
    exit()

def myIntInput(string:str="", maxInt:int=10):
    while 1:
        try:
            var = int(input(f"Введите кол-во{string}:\n> "))
            if var <= 0:
                print(f"Кол-во{string} должно быть больше 0.")
                continue
            if var > maxInt:
                print(f"Слишком большое число! (Max: {maxInt})")
                continue
            return var
        except ValueError: print("Неправильно введено целое число")
        except (EOFError,KeyboardInterrupt): cexit()
        except Exception as e: print(e, "\n\n\nПроизошла ошибка, проверьте свой ввод")

#region Rows
matrixRows = 0
matrixRows = myIntInput(" строк в матрице", maxNum)
#endregion

#region Elements
matrixElems = 0
matrixElems = myIntInput(" элементов в строке матрицы", maxNum)
#endregion

matrix = [
    [randint(min_range, max_range) for elem in range(matrixElems)] 
    for row in range(matrixRows)
]
print("Исходая матрица:\n"+("\n".join(map(str, matrix)))+"\n")

sb = [
    f"[{i}] {sum(line)}/{len(line)} = {sum(line)/len(line)} ({', '.join( map(str, line) )})" 
    for i, line in enumerate(matrix, 1) 
    if i % 2 == 1
]
print("\n".join(sb))