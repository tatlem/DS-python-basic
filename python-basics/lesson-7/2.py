"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.

Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.

Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать
абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

"""


class Clothes:
    def __init__(self, name, fabric_consumption):
        self.name = str(name)
        self.fabric_consumption = fabric_consumption

    def __str__(self):
        return '{:10} has fabric consumption {:.2f}'.format(self.name, self.fabric_consumption)

    def __add__(self, other):
        return self.fabric_consumption + other.fabric_consumption


class Coat(Clothes):
    @property
    def fabric_consumption(self):
        return self.__fabric_consumption

    @fabric_consumption.setter
    def fabric_consumption(self, fabric_consumption):
        self.__fabric_consumption = (fabric_consumption / 6.5) + 0.5


class Suit(Clothes):
    @property
    def fabric_consumption(self):
        return self.__fabric_consumption

    @fabric_consumption.setter
    def fabric_consumption(self, fabric_consumption):
        self.__fabric_consumption = (fabric_consumption * 2) + 0.3


coat = Coat('Пальто', 10)
suit = Suit('Костюм', 20)
print(coat)
print(suit)
print('-----\nOverall fabric consumption is {:.2f}'.format(coat + suit))
