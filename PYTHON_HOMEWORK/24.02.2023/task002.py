"""
Задание 2:
Создать метакласс для паттерна Синглтон
"""


class Singleton(type):
    value = None

    def __call__(cls, *args, **kwargs):
        if cls.value is None:
            cls.value = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.value


class Worker(metaclass=Singleton):
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
position_02 = Position('Alex', 'Moss', 'accountant', 1800, 0)

print(position_01)
print(position_02.get_full_name(), position_02.position,
      position_02.get_total_income())
