# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

import math

seconds_all = int(input('Type seconds: '))

hours = math.floor(seconds_all / 60 / 60)
minutes = math.floor((seconds_all - (hours * 60 * 60)) / 60)
seconds = seconds_all - (hours * 60 * 60) - (minutes * 60)

if hours < 10:
    hours = '0' + str(hours)

if minutes < 10:
    minutes = '0' + str(minutes)

if seconds < 10:
    seconds = '0' + str(seconds)

print(f"Converting to time is {hours}:{minutes}:{seconds}")
