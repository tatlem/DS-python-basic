# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

num = int(input('Type integer: '))
num_string = str(num)
result = num + int(num_string + num_string) + int(num_string + num_string + num_string)
print(result)