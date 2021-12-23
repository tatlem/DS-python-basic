# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает
# фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

profit = int(input('Type profit ($): '))
costs = int(input('Type costs ($): '))
# profit = 100
# costs = 75

balance = profit - costs

if balance > 0:
    print('Good! Yours profit is grater than costs')

    earnings = balance
    profitability = (earnings / profit) * 100
    print(f'Profitability rate is {profitability:.0f}%')

    employees = int(input('Type number of employees: '))
    profit_per_employee = profit / employees
    print(f'Profit per employee is ${profit_per_employee:.2f}')


elif balance == 0:
    print('Not bad. Yours profit equals costs')
else:
    print('Bad! Yours costs is grater than profit')
