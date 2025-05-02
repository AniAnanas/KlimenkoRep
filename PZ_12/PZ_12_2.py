"""Вариант 13.
2. Составить список, в который будут включены только согласные буквы и привести
их к верхнему регистру. Список: ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели',
'Каир'].
"""
origList = ['Оттава', 'Москва', 'Пекин', 'Полоцк', 'Версаль', 'Дели',
'Каир']
glas = {"а", "е", "ё", "и", "о", "у", "ы", 'э', "ю", "я"}
print([i.upper() for i in "".join(origList) if i.lower() not in glas])

lastList = [
    "".join(
        [ char.upper() for char in slovo if char.lower() not in glas ]
    ) for slovo in origList ]

print(lastList)