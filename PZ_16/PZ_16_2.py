"""Вариант 13.
Создайте базовый класс "Человек" со свойствами "имя", "возраст" и "пол". От этого
класса унаследуйте классы "Мужчина" и "Женщина" и добавьте в них свойства,
связанные с социальным положением (например, "семейное положение",
"количество детей" и т.д.)."""

class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

class Man(Human):
    def __init__(self, name, age, sex, family_status, children):
        super().__init__(name, age, sex)
        self.family_status = family_status
        self.children = children

class Woman(Human):
    def __init__(self, name, age, sex, family_status, children):
        super().__init__(name, age, sex)
        self.family_status = family_status
        self.children = children
        