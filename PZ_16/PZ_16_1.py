"""Вариант 13.
Создайте класс "Компьютер" с атрибутами "марка", "процессор" и "оперативная
память". Напишите метод, который выводит информацию о компьютере в формате
"Марка: марка, Процессор: процессор, Оперативная память: память"."""


class Computer:
    def __init__(self, brand, processor, memory):
        self.brand = brand
        self.processor = processor
        self.memory = memory
        
    def __str__(self):
        return f"Марка: {self.brand}, Процессор: {self.processor}, Оперативная память: {self.memory}"

comp1 = Computer("MSI", "Ryzen 7 5700X 8-core processor", "16GB DDR4 3200MHz")
comp2 = Computer("Gigabyte", "Intel Core i7 14700KF", "64GB DDR5 7200MHz")

print(comp1)
print(comp2)