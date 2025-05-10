"""Вариант 13.
1. Для каждой строки матрицы с нечетным номером найти среднее арифметическое ее элементов.
"""
from random import randint
maxNum = 5

def cexit():
    print("Bye!\r", end="")
    exit()

matrixRows = 0
#region Rows
while 1:
    try:
        matrixRows = int(input("Введите кол-во строк в матрице:\n> "))
        if matrixRows <= 0:
            print("Кол-во элементов должно быть больше 0.")
            continue
        if matrixRows > maxNum:
            print(f"Слишком большое число! (Max: {maxNum})")
            continue
        break
    except ValueError: print("Неправильно введено целое число")
    except EOFError: cexit()
    except KeyboardInterrupt: cexit()
    except Exception as e: print(str(e.with_traceback())+"\n\n\nПроизошла ошибка, проверьте свой ввод")
#endregion

matrixElems = 0
#region Elements
while 1:
    try:
        matrixElems = int(input("Введите кол-во элементов в строке матрицы:\n> "))
        if matrixElems <= 0:
            print("Кол-во элементов должно быть больше нуля!")
            continue
        if matrixElems > maxNum:
            print(f"Слишком большое число! (Max: {maxNum})")
            continue
        break
    except ValueError: print("Неправильно введено целое число")
    except EOFError: cexit()
    except KeyboardInterrupt: cexit()
    except Exception as e: print(e.__str__()+"\n\n\nПроизошла ошибка, проверьте свой ввод")
#endregion

matrix = [[randint(-100,100) for elem in range(matrixElems)] for row in range(matrixRows)]
s = [f"[{i}] {sum(line)} ({', '.join(map(str, line))})" for i, line in enumerate(matrix, 1) if i % 2 == 1]
print("\n".join(s))