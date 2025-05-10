"""Вариант 13.
В двумерном списке найти максимальный положительный элемент кратный 4."""
from random import randint
maxNum = 5

def cexit():
    print("Bye!\r", end="")
    exit()

matrixRows = 0
while 1:
    try:
        matrixRows = int(input("Введите кол-во строк в матрице:\n> "))
        if matrixRows < 1:
            print("Кол-во строк должно быть больше 0.")
            continue
        if matrixRows > maxNum:
            print(f"Слишком большое число! (Max: {maxNum})")
            continue
        break
    except ValueError: print("Неправильно введено целое число")
    except KeyboardInterrupt: cexit()
    except EOFError: cexit()
    except Exception as e: print(e.__str__()+"\n\n\nПроизошла ошибка, проверьте свой ввод")
        
matrixElems = 0
while 1:
    try:
        matrixElems = int(input("Введите кол-во элементов в строке матрицы:\n> "))
        if matrixElems < 1:
            print("Кол-во элементов должно быть больше 0.")
            continue
        if matrixElems > maxNum:
            print(f"Слишком большое число! (Max: {maxNum})")
            continue
        break
    except ValueError: print("Неправильно введено целое число")
    except KeyboardInterrupt: cexit()
    except EOFError: cexit()
    except Exception as e: print(e.__str__()+"\n\n\nПроизошла ошибка, проверьте свой ввод")

matrix = [[randint(-100,100) for j in range(matrixElems)] for i in range(matrixRows)]
print("\n".join(map(str,matrix)))
 
vmax = -float("inf")
indexes = []
for row in matrix:
    filt = list(filter(lambda x: x%4==0, row))
    if filt != [] and vmax < max(filt):
        vmax = max(filt)
        indexes = [matrix.index(row), row.index(max(filt))]
print(f"Максимальный положительный элемент: {vmax}\nРасположен он в {indexes[0]+1} строке, {indexes[1]+1} столбце")
