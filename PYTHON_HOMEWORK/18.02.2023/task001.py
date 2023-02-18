"""
Задание 1:

Создать класс TrafficLight (светофор) и определить у него один приватный
атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета используйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""

from time import sleep


class TrafficLight:
    __color = f'\033[31m{"red"}'

    def running(self):
        print(self.__color)
        sleep(7)
        self.__color = f'\033[33m{"yellow"}'
        print(self.__color)
        sleep(2)
        self.__color = f'\033[32m{"green"}'
        print(self.__color)
        sleep(7)
        self.__color = f'\033[31m{"red"}'
        # скрипт осуществляет бесконечное выполнение до ручного прерывания
        self.running()


traffic_light = TrafficLight()
traffic_light.running()
