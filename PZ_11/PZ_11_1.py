from os import path
from random import randint
from typing import List 
import logging

strfmt = '[%(asctime)s][%(name)s][%(levelname)s] > %(message)s'
datefmt = '%d-%m-%Y %H:%M:%S'
formatter = logging.Formatter(fmt=strfmt, datefmt=datefmt)

stream = logging.StreamHandler()
stream.setFormatter(formatter)
# stream.setLevel(logging.INFO)
stream.setLevel(logging.DEBUG)

logger = logging.getLogger("logg")
logger.setLevel(logging.DEBUG)
logger.addHandler(stream)

target_digits = -1

MyDir = path.dirname(path.abspath(__file__))
DigitsPath = path.join(MyDir, "digits.txt")
TextOutputPath = path.join(MyDir, "output.txt")

while target_digits < 1:
    try: 
        target_digits = int(input("Введите количество чисел: ").strip())
        if target_digits > 0:
            break
        print("Кол-во чисел должно быть больше 0, повторите попытку")
    except Exception as e: 
        print("Неверно ввели число, повторите попытку.")
        logger.error("Ошибка: {}".format(e.__str__()))
try:
    with open(DigitsPath, "w") as file1:
        text = ""
        for _ in range(0, target_digits):
            text += str(randint(-100,100))+" "
            
        file1.write(text)
        logger.debug(f"Файл {file1.name} создан с текстом: {text}")
except Exception as e: logger.error("Не удалось записать файл, {}".format(e))

def mult(a:List[int]) -> int:
    logger.debug(f"<function mult> вызвана со списком: {a}")
    
    m = 1
    for el in a:
        m *= el
    return m

try:
    with open(DigitsPath, "r") as file1:
        listd:List[int] = list(map(int, file1.readline().split()))
        listlen = float(listd.__len__())
        start_index, end_index =  int(listlen/3), int( listlen-(listlen/3))
        try:
            with open(TextOutputPath, "w") as output:
                text = f"""Исходные данные: {listd}
Количество элементов: {int(listlen)}
Индекс первого максимального элемента: {listd.index(max(listd))}
Произведение элементов средней трети: {mult( listd[start_index:end_index] )}"""
                output.write(text)
                
                logger.debug(f"Создан файл в {path.join(MyDir, output.name)}\nТекст файла >>")
                logger.info("\n"+text)
        except Exception as e: logger.error("Не удалось записать файл, {}".format(e))
except Exception as e: logger.error("Не удалось прочитать файл, {}".format(e))

logger.debug("Программа завершила работу.")