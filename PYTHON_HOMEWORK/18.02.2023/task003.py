"""
Задание 3:

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например,
{"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position
реализовать публичные методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса
Position, передать данные, проверить значения атрибутов, вызвать методы
экземпляров).

П.С. попытайтесь добиться вывода информации о сотруднике также через перегрузку
str
str(self) - вызывается функциями str, print и format. Возвращает строковое
представление объекта.
"""


class Worker:
    def __init__(self, first_name, last_name, position, salary, bonus):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.income = {'salary': salary, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def get_total_income(self):
        return self.income['salary'] + self.income['bonus']

    def __str__(self):
        return f'{self.get_full_name()}, {self.get_total_income()} USD'


position_01 = Position('John', 'Smith', 'lawyer', 1500, 500)

print(position_01.first_name, position_01.last_name, position_01.position)
print(position_01.income)
print(position_01.get_full_name(), position_01.get_total_income())
print(position_01)
