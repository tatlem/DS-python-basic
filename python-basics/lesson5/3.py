# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

f = open('3.txt', 'r')

lines = f.readlines()
overall_salary = 0
overall_employees = len(lines)

for line in lines:
    salary, fio = line.split(maxsplit=1)
    salary = int(salary)
    fio = fio.strip()
    overall_salary += salary

    if salary >= 20000:
        print(fio, 'has big salary')

f.close()

avg_salary = overall_salary / overall_employees

print('-' * 20)
print('Average salary is', avg_salary)
