"""Вариант 13.
В двумерном списке найти максимальный положительный элемент кратный 4."""
from random import randint
maxNum = 20

def cexit():
    print("Bye!\r", end="")
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

matrix = [[randint(-100,100) for j in range(matrixElems)] for i in range(matrixRows)]
print("\n".join(map(str,matrix)))

vmax = -float("inf")
indexes = []
for row in matrix:
    filt = list(filter(lambda x: x%4==0, row))
    if filt != [] and vmax < max(filt):
        vmax = max(filt)
        indexes = [matrix.index(row), row.index(max(filt))]
print(f"Максимальный положительный элемент: {vmax}\nРасположен в {indexes[0]+1} строке, {indexes[1]+1} столбце")
