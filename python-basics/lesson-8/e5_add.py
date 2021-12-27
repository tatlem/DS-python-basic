"""
5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
а также других данных, можно использовать любую подходящую структуру, например словарь.
"""

import e4_sklad


class Store(e4_sklad.StoreBase):
    def put(self, item):
        self.items.update({item.id: item})
        self.positions.append(item.id)

    def put_multi(self, item):
        amount = int(input(f'Введите кол-во штук {item.name} для зачисления на склад: '))

        if amount > 0:
            for i in range(amount):
                self.put(item)

    def get(self, item):
        return self.items[item.id]

    def remove(self, item):
        try:
            self.positions.remove(item.id)
        except ValueError as err:
            print(f'Ошибка {item.name} нет на складе, чтобы убрать')
        else:
            if self.positions.count(item.id) == 0:
                del self.items[item.id]

    def move(self, item_, to):
        item = self.get(item_)
        self.remove(item)
        print(f'{item.name} has moved to {to}')


# printer = e4_sklad.PrinterEquipment(1, 'Принтер', 10.2)
# scanner = e4_sklad.ScannerEquipment(2, 'Сканер', 2, 100)
# # xerox = e4_sklad.XeroxEquipment(3, 'Ксерокс', 4)
#
# store = Store()
#
# store.put(printer)
# # store.put(printer)
# # store.put(printer)
# # store.put_multi(printer)
# # store.remove(printer)
# # store.remove(printer)
# # store.remove(printer)
#
# store.put(scanner)
# store.move(scanner, 'Министерство правды')
#
# print(store)
