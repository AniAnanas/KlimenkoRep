"""Вариант 13.
1.Проверить есть ли в последовательности целых N чисел число K.
"""
from random import randint
from itertools import tee
from typing import Generator

#region Definitions
def isNumInIter(value:int, iterator:Generator):
    for item in iterator:
        if item == value:
            return True
    return False

def exitProgram():
    print("Выход...\r", end="")
    exit()
#endregion

#region Inputs
numbersCount = 0
targetValue = ''

while numbersCount <= 0:
    try:
        numbersCount = int(input("Введите количество чисел в списке.\n> ").strip())
        if numbersCount <= 0: print("Кол-во чисел должно быть больше 0!")
    except ValueError:
        print("Неправильно ввели целое число.")
        continue
    except EOFError:exitProgram()
    except KeyboardInterrupt:exitProgram()
    except Exception as e: print(f"{e}\n\nПроизошла ошибка! Проверьте свой ввод целого числа.")
    
while type(targetValue) == str:
    try:targetValue = int(input("Введите число для поиска.\n> ").strip())
    except ValueError:
        print("Неправильно ввели целое число.")
        continue
    except EOFError:exitProgram()
    except KeyboardInterrupt:exitProgram()
    except Exception as e: print(f"{e}\n\nПроизошла ошибка! Проверьте свой ввод целого числа.")
#endregion

genList = (randint(-100,100) for i in range(numbersCount))
genList, gen2Print = tee(genList)
print("Сгенерированный список: " + ", ".join(map(str,gen2Print)))

message = "Число " + str(targetValue) + " в последовательности "
message += "присутствует" if isNumInIter(targetValue, genList) else "отсутствует"
print(message)

del numbersCount, targetValue, genList, message, gen2Print