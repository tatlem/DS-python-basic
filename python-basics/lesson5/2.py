# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.

f = open('2.txt', 'r')

lines = f.readlines()

for line in lines:
    words = line.split(' ')
    print('Words are in row:', len(words))

f.close()

print('Overall lines are', len(lines))
