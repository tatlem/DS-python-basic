# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

f = open('1.txt', 'w')

while True:
    data = input('Enter string (empty string to exit): ')

    if data:
        f.write(data + '\n')
    else:
        break

f.close()
