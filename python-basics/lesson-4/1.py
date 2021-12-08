# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах * ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, working_hours, rate_per_hour, bonus = argv
working_hours = float(working_hours)
rate_per_hour = float(rate_per_hour)
bonus = float(bonus)
earnings = (working_hours * rate_per_hour) + bonus
print('Earnings is', earnings)
