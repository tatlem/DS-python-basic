# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы
# с индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

# list_ = ['a', 'b', 'c', 'd', 'e', 'f']

input_str = input('Input values divided by comma (example: 1,2,3,4,5): ')
list_ = input_str.split(',')

print('current list is ', list_)

i = 0
length = len(list_)
list2 = []

while i < length:
    if i + 1 < length:
        list2.append(list_[i + 1])

    list2.append(list_[i])
    i += 2

print('modified list is', list2)
