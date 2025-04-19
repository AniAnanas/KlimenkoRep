"""Вариант 13.
1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
последовательность из целых положительных и отрицательных чисел. Сформировать
новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
обработку элементов:

Исходные данные:
Количество элементов:
Индекс первого максимального элемента:
Произведение элементов средней трети:
"""

from os import path
from random import randint
from typing import List 
import logging

#region Logging
strfmt = '[%(asctime)s][%(name)s][%(levelname)s] > %(message)s'
datefmt = '%d-%m-%Y %H:%M:%S'
formatter = logging.Formatter(fmt=strfmt, datefmt=datefmt)

stream = logging.StreamHandler()
stream.setFormatter(formatter)
stream.setLevel(logging.INFO)
# stream.setLevel(logging.DEBUG)

logger = logging.getLogger("logg")
logger.setLevel(logging.DEBUG)
logger.addHandler(stream)
#endregion Logging

def mult(a:List[int]) -> int:
    logger.debug(f"<function mult> вызвана со списком: {a}")
    
    m = 1
    for el in a:
        m *= el
    return m

targetDigits = -1

scriptDir = path.dirname(path.abspath(__file__))
digitsPath = path.join(scriptDir, "digits.txt")
textOutputPath = path.join(scriptDir, "output.txt")

while targetDigits < 1:
    try: 
        targetDigits = int(input("Введите количество чисел: ").strip())
        if targetDigits > 0:
            break
        print("Кол-во чисел должно быть больше 0, повторите попытку")
        
    except ValueError: print("Неверно ввели число, повторите попытку.")
    except KeyboardInterrupt: print("\r", end="") or exit()
    except EOFError: print("\r", end="") or exit()
    except Exception as e: 
        print("Произошла ошибка, повторите попытку.")
        logger.error(f"Ошибка: {e}")

try:
    with open(digitsPath, "w") as file1:
        text = ""
        for _ in range(0, targetDigits):
            text += str(randint(-100,100))+" "
            
        file1.write(text)
        logger.debug(f"Файл {file1.name} создан с текстом: {text}")
except Exception as e: logger.error("Не удалось записать файл, {}".format(e))

try:
    with open(digitsPath, "r") as file1:
        listd:List[int] = list(map(int, file1.readline().split()))
        listlen = float(listd.__len__())
        start_index, end_index =  int(listlen/3), int( listlen-(listlen/3))
        try:
            with open(textOutputPath, "w") as output:
                text = f"""Исходные данные: {listd}
Количество элементов: {int(listlen)}
Индекс первого максимального элемента: {listd.index(max(listd))}
Произведение элементов средней трети: {mult( listd[start_index:end_index] )}"""
                output.write(text)
                
                logger.debug(f"Создан файл в {path.join(scriptDir, output.name)}")
                logger.info("Текст файла >>\n"+text)
        except Exception as e: logger.error(f"Не удалось записать файл, ошибка: {e}")
except Exception as e: logger.error(f"Не удалось прочитать файл, ошибка: {e}")

logger.debug("Программа завершила работу.")