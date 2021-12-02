# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.

# month_input = 12
month_input = int(input('Input number of month: '))

if month_input < 1 or month_input > 12:
    exit('Wrong month number')

# via dict
print('--- via dict ---')
seasons = dict(winter=(12, 1, 2), spring=(3, 4, 5), summer=(6, 7, 8), autumn=(9, 10, 11))
isMonthDefined = False

for season in seasons:
    seasonMonths = seasons.get(season)

    for seasonMonth in seasonMonths:
        if month_input == seasonMonth:
            print(f'Month num {month_input} is in {season} season')
            isMonthDefined = True
            break

    if isMonthDefined:
        break

# via list
print('--- via list ---')
seasons = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn', 'autumn', 'autumn',
           'winter']
print(f'Month num {month_input} is in {seasons[month_input - 1]} season')
