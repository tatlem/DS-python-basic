"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно
обработать эту ситуацию и не завершиться с ошибкой.
"""


class ExceptionMyZero(Exception):
    def __init__(self, txt):
        self.txt = txt


inp_data = input("На что разделим 100: ")

try:
    inp_data = int(inp_data)

    if inp_data == 0:
        raise ExceptionMyZero('Ой')

    print(100 / inp_data)

except ExceptionMyZero as err:
    print(err)

print('-- Конец программы --')
