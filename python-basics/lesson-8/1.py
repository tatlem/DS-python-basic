"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""


class Date:
    def __init__(self, day=1, month=1, year=2021):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def set_date_from_str(cls, date_str):
        day, month, year = cls.parse_date_from_str(date_str)
        return cls(day, month, year)

    @staticmethod
    def parse_date_from_str(date_str):
        chunks = date_str.split('-')
        data = []

        for chunk in chunks:
            if chunk:
                data.append(int(chunk))

        day, month, year = data

        return day, month, year

    @staticmethod
    def is_valid(date_str):
        day, month, year = Date.parse_date_from_str(date_str)
        return day <= 31 and month <= 12 and 2000 < year < 2100


date_1 = Date.set_date_from_str('01-01-2022')
print(Date.is_valid('01-01-2000'))
print(Date.is_valid('01-01-2001'))
print(date_1.is_valid('01-01-20000'))
print(date_1.is_valid('01-01--20000'))
print(date_1.is_valid('31-01-2022'))
print(date_1.is_valid('01-13-2022'))
# print(date_1.is_valid('01'))
