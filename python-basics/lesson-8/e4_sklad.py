"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
уникальные для каждого типа оргтехники.
"""


class OfficeEquipment:
    def __init__(self, id, name, weight):
        self.id = id
        self.set_name(name)
        self.set_weight(weight)

    def set_name(self, name):
        self.name = str(name)

    def set_weight(self, weight):
        self.weight = float(weight)

    def __str__(self):
        return f'{self.name} has weight {self.weight} kg(s)'


class PrinterEquipment(OfficeEquipment):
    pass


class ScannerEquipment(OfficeEquipment):
    def __init__(self, id, name, weight, speed):
        super().__init__(id, name, weight)
        self.speed = int(speed)


class XeroxEquipment(OfficeEquipment):
    pass


class StoreBase:
    def __init__(self):
        self.items = {}
        self.positions = []

    def __str__(self):
        return f'Items in store: {self.positions} => {str(self.items)}'
