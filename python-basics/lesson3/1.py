# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def division(int1, int2):
    if int1 == 0 or int2 == 0:
        return 'Division by zero is prohibited!'

    return int1 / int2


int1 = int(input('Input integer 1: '))
int2 = int(input('Input integer 2: '))

print(division(int1, int2))
