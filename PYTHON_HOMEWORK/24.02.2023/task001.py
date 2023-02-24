"""
Задание 1:
Создать не менее двух дескрипторов для атрибутов классов, которые вы создали
ранее в ДЗ
"""


class NotNegative:
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Значение не может быть отрицательным')
        instance.__dict__[self.attribute] = value

    def __set_name__(self, owner, attribute):
        self.attribute = attribute


class NotNullValue:
    def __set__(self, instance, value):
        if value == 0:
            raise ValueError('Значение не может быть нулевым')
        if value < 0:
            raise ValueError('Значение не может быть отрицательным')
        instance.__dict__[self.attribute] = value

    def __set_name__(self, owner, attribute):
        self.attribute = attribute


class CheckName:
    def __get__(self, instance, value):
        return instance.__dict__[self.attribute]

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise TypeError('Значение должно быть типа str')
        instance.__dict__[self.attribute] = value

    def __delete__(self, instance):
        raise AttributeError('Невозможно удалить атрибут')

    def __set_name__(self, owner, attribute):
        self.attribute = attribute


class Worker:
    first_name, last_name = CheckName(), CheckName()
    salary = NotNullValue()
    bonus = NotNegative()

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

delattr(position_01, 'last_name')
