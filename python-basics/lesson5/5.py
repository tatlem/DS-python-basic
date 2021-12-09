# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
from functools import reduce

numbers = list(range(1, 11))

f = open('5.txt', 'w')
f.write(' '.join(str(num) for num in numbers))
f.close()

# get numbers from file
f = open('5.txt')
data = f.read()
numbers = data.split(' ')

print('Numbers are', numbers)
print('Sum is', reduce(lambda x, y: int(x) + int(y), numbers))

