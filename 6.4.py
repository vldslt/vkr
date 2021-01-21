'''
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать,
что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость
автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение
о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов.
Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''


class Car:
    def __init__(self,
            color: str,
            name: str,
            is_police: bool = False):
        self.color = color
        self.name = name
        self.is_police = True if is_police else False
        self.speed = 0
        self._direction = ''
    def go(self, speed: float):
        try:
            self.speed = float(speed)
        except ValueError:
            pass
    def stop(self):
        self.speed = 0
    def turn(self, direction: str):
        if direction not in ('left', 'right'):
            print(f"'{direction}' invalid direction")
            return
        if not self.speed:
            print(f"'Cant turn to {direction}'")
            return
        self._direction = direction
    def show_speed(self):
        print(f'My speed {self.speed} km/h')
        if (hasattr(self, '_max_granted_speed')
                and self._max_granted_speed
                and self.speed > self._max_granted_speed):
            print(f'Over speed on {self.speed - self._max_granted_speed} km/h')
    def direction(self):
        return self._direction

class TownCar(Car):
    _max_granted_speed = 60
class SportCar(Car):
    pass
class WorkCar(Car):
    _max_granted_speed = 40
class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args, is_police=True)
