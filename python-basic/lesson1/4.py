# 4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

num = int(input('Type positive integer: '))
num_string = str(num)

i = 0
num_max = 0

while i < len(num_string):
    digit = int(num_string[i])

    if num_max < digit:
        num_max = digit

    i = i + 1

print('The largest digit is', num_max)
