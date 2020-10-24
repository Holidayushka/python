"""5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw.
Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра."""
class Stationery():
    def __init__(self, title):
        self.title = title
    def draw(self):
        return f"Starting drawing"

class Pen(Stationery):
    def draw(self):
        return f"{super().draw()} with pen"

class Pencil(Stationery):
    def draw(self):
        return f"{super().draw()} with pencil"

class Handle(Stationery):
    def draw(self):
        return f"{super().draw()} with handle"

s1 = Pen("pen")
s2 = Pencil("pencil")
s3 = Handle("handle")
print(s1.draw())
print(s2.draw())
print(s3.draw())