# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

list_source = [el for el in range(100, 1001)]
list_multi = reduce(lambda x, y: x * y, list_source)

print('Source list is', list_source)
print('Multiplied list is', list_multi)
