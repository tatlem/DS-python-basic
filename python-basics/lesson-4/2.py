"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""
import random

# static list
# list_source = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# generate random list
list_source = []

for i in range(0, random.randint(2, 20)):
    list_source.append(i * random.randint(0, 10))

# generate modified list
list_mod = [item for item in list_source
            if list_source.index(item) != 0 and item > list_source[list_source.index(item) - 1]]

print('Source list is', list_source)
print('Modified list is', list_mod)
