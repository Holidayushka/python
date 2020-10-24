"""4. Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости."""

class Car():
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        return f"{self.name} is moving"
    def stop(self):
        return f"{self.name} stopped"
    def turn(self, side):
        return f"{self.name} turned to {side}"
    def show_speed(self):
        return self.speed

class TownCar(Car):
    def show_speed(self):
        if super().show_speed() > 60:
            print("You are speeding")
        return f"Speed: {super().show_speed()}"
class WorkCar(Car):
    def show_speed(self):
        if super().show_speed() > 40:
            print("You are speeding")
        return f"Speed: {super().show_speed()}"

class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

car_1 = TownCar(70, "red", "mazda", False)
print(car_1.turn("right"))
print(car_1.show_speed())

car_2 = WorkCar(50, "red", "ford", False)
print(car_2.turn("left"))
print(car_2.show_speed())