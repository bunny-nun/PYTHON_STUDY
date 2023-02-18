"""
Задание 2:

Реализовать класс Road (дорога), в котором определить защищенные атрибуты:
length (длина в метрах), width (ширина в метрах).

Значения данных атрибутов должны передаваться при создании экземпляра класса.

Реализовать публичный метод расчета массы асфальта, необходимого для покрытия
всего дорожного полотна.

Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв.
метра дороги асфальтом, толщиной в 1 см * число м толщины полотна.
Массу и толщину сделать публичными атрибутами. Проверить работу метода.

Например: 20м * 5000м * 25кг * 0.05м = 125000 кг = 125 т
"""


class Road:
    weight = 25
    height = 0.05

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_weight(self):
        return int(self._length * self._width * self.weight * self.height)

    def __str__(self):
        return f'{self._length}m * {self._width}m * {self.weight}kg * {self.height}m = {self.road_weight()}kg = {int(self.road_weight() / 1000)}t'


road = Road(20, 5000)
print(road)
print(road.road_weight())
