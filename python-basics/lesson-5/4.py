"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

f = open('4.txt')
numbers_ru = {
    1: 'Один',
    2: 'Два',
    3: 'Три',
    4: 'Четыре',
    5: 'Пять',
    6: 'Шесть',
    7: 'Семь',
    8: 'Восемь',
    9: 'Девять',
    0: 'Ноль',
}
lines_new = []
delim = ' — '

for line in f.readlines():
    title_en, num = line.split(delim)
    num = int(num.strip())
    title_ru = numbers_ru[num]
    lines_new.append(f'{title_ru}{delim}{num}')

f.close()

data = '\n'.join(lines_new)

f_mod = open('4_mod.txt', 'w')
f_mod.write(data)

print(data)

