"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

f = open('6.txt')
lessons = {}

for line in f.readlines():
    lesson_title, lessons_raw = line.split(':')
    lessons_count = 0

    # count lessons
    words = lessons_raw.split(' ')

    for word in words:
        word = word.strip()

        if word and word != '—':
            hours, _tmp = word.split('(', maxsplit=1)
            hours = int(hours)
            lessons_count += hours

    # add lesson to dict
    lessons[lesson_title] = lessons_count

print(lessons)
