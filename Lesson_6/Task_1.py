"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод."""
from time import sleep
from itertools import cycle

class TrafficLight:
    __colour_list = ["red", "yellow", "green"]
    def running(self):
        print("Starting...")
        count = 0
        for colour in cycle(TrafficLight.__colour_list):
            if count > 6:
                break
            if colour == "red":
                count += 1
                print("red")
                sleep(7)
            elif colour == "yellow":
                count += 1
                print("yellow")
                sleep(2)
            else:
                print("green")
                count += 1
                sleep(4)

TrafficLight().running()