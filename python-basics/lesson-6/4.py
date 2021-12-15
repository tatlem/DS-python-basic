"""
4. Реализуйте базовый класс Car.

у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Вызовите методы и покажите результат.

"""


class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = int(speed)
        self.color = str(color)
        self.name = str(name)
        self.is_police = bool(is_police)

    def go(self, go_mode_title='поехала'):
        print(f'{self.name} {go_mode_title} {self.get_speed()}')

        if self.is_police:
            print('...и включила сирену')

    def stop(self):
        print(f'{self.name} остановилась')

        if self.is_police:
            print('...как вкопанная')

    def turn(self, direction='L'):
        if direction == 'L':
            direction_title = 'лево'
        else:
            direction_title = 'право'

        print(f'{self.name} поворачивает на{direction_title} {self.get_speed()}')

    def get_speed(self):
        if self.speed > 300:
            print(f'{self.name} быстрее ветра?')
            raise ValueError

        return f'со скоростью {self.speed} км/ч'

    def show_speed(self):
        print(self.get_speed())


class TownCar(Car):
    def get_speed(self):
        if self.speed > 60:
            print(f'{self.name} не может так быстро ехать')
            raise ValueError

        return f'со скоростью {self.speed} км/ч'


class SportCar(Car):
    pass


class WorkCar(Car):
    def get_speed(self):
        if self.speed > 40:
            print(f'{self.name} не может так быстро ехать')
            raise ValueError

        return f'со скоростью {self.speed} км/ч'


class PoliceCar(Car):
    pass


try:
    car_base = Car(1, 'Черная', 'Колымага')
    car_base.go()
    car_base.turn('L')
    car_base.turn('R')

    print('-' * 20)

    car_town = TownCar(40, 'Белая', 'Телега')
    car_town.go()

    print('-' * 20)

    car_sport = SportCar(300, 'Красная', 'Ракета')
    car_sport.go('полетела')

    print('-' * 20)

    car_work = WorkCar(40, 'Черная', 'Моя ласточка')
    car_work.go()

    print('-' * 20)

    car_work = PoliceCar(150, 'Белая с синей полосой', 'Полиция', 1)
    car_work.go('устремилась')
    car_work.turn()
    car_work.stop()

except ValueError:
    print('Ненене! Тише едешь - дальше будешь!')
