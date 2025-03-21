from random import randint
from typing import List 

target_digits = -1

while target_digits < 1:
    try: 
        target_digits = int(input("Введите количество чисел: ").strip())
        if target_digits > 0:
            break
        print("Кол-во чисел должно быть больше 0, повторите попытку")
    except Exception as e: print("Неверно ввели число, повторите попытку.")

with open("digits.txt", "w") as file1:
    text = ""
    for _ in range(0, target_digits):
        text += str(randint(-100,100))+" "
    file1.write(text)
    print(f"[DEBUG] Файл {file1.name} создан с текстом: [{text}]")

def mult(a:List[int]) -> int:
    print(f"[DEBUG] <function mult> вызвана со списком: {a}")
    m = 1
    for el in a:
        m *= el
    return m

with open("digits.txt", "r") as file1:
    listd:List[int] = list(map(int, file1.readline().split()))
    listlen = float(listd.__len__())
    start_index, end_index =  int(listlen/3), int( listlen-(listlen/3))
    with open("output.txt", "w") as output:
        output.write(f"""Исходные данные: {listd}
Количество элементов: {int(listlen)}
Индекс первого максимального элемента: {listd.index(max(listd))}
Произведение элементов средней трети: {mult( listd[start_index:end_index] )}""")

print("[DEBUG] Программа завершила работу.")