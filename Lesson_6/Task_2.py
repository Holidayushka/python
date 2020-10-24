"""2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса.
Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т"""
class Road:
    def __init__(self, lenght, width, height, mass_for_1_cm):
        self._lenght = lenght
        self._width = width
        self._height = height
        self._mass_for_1_cm = mass_for_1_cm
    def calculations(self):
        return self._lenght * self._width * self._height * self._mass_for_1_cm
road = Road(10, 20, 10, 20)
print(road.calculations())
