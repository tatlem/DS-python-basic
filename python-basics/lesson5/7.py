"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить
-прибыль каждой компании, а также
-среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. н должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""

try:
    with open('7.txt') as f_obj:
        average_profit = 0
        overall_profit = 0
        overall_firms = 0
        firms = {}

        # calc
        for line in f_obj:
            firm_title, property_form, income, costs = line.split()
            income = int(income)
            costs = int(costs)
            balance = income - costs
            profit = 0

            if balance > 0:
                profit = balance
                overall_profit += profit
                overall_firms += 1

            # save to list
            firms[firm_title] = balance

        if overall_profit > 0 and overall_firms > 0:
            average_profit = overall_profit / overall_firms

        # export to file
        data = [firms, {'average_profit': average_profit}]
        print(data)
        f = open('7_result.txt', 'w')
        f.write(str(data))
        f.close()
except IOError:
    print("Произошла ошибка ввода-вывода!")
