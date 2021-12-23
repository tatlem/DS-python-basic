"""
6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""
import e4_sklad
import e5_add


class StoreWithFilter(e5_add.Store):
    def put_multi(self, item):
        while True:
            try:
                super().put_multi(item)
            except ValueError:
                print('Только число!')
            else:
                break


store = StoreWithFilter()
xerox = e4_sklad.XeroxEquipment(3, 'Ксерокс', 4)
store.put_multi(xerox)

print(store)
