"""6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который
общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b
и выводить одно натуральное число — номер дня.

Например: a = 2, b = 3.
Результат:

1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""

km_initial = int(input('Type amount of km on first day: '))
km_target = int(input('Type target amount of km: '))
day = 1
km_sum = km_initial

if km_initial <= 0 or km_target <= 0:
    exit('Wrong input data! You must use positive integer values only')

while km_sum < km_target:
    km_sum = km_sum + (km_sum * 0.1)
    day = day + 1

print(f'You will reach target km in {day} day(s)')
