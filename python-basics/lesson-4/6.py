"""
6. Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным. Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.
"""
from random import randint
from itertools import count, cycle

# a
# start = int(input('Start from:'))
#
# for i in count():
#     if i == 10:
#         break
#     elif i >= start:
#         print(i)

# b
print('--- Relations generator ---')
boys = ['Roman', 'Sergey', 'Ivan']
girls = ['Tanya', 'Svetlana', 'Anna', 'Katya']
relations = ['hate', 'love']

while True:
    key = input('Press q for exit or Enter for generate relations: ')

    if key == 'q':
        break

    boy = boys[randint(0, len(boys) - 1)]
    girl = girls[randint(0, len(girls) - 1)]
    relation = relations[randint(0, len(relations) - 1)]
    print(boy, '+', girl, '=', relation)
