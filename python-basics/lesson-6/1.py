"""
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
(зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение
и завершать скрипт.
"""
import time


class TrafficLight:
    # color duration seconds
    __colors_config_default = {'red': 3, 'orange': 2, 'yellow': 1, 'green': 4}

    __colors_config = {'red': __colors_config_default['red'],
                       'orange': __colors_config_default['orange'],
                       'yellow': __colors_config_default['yellow'],
                       'green': __colors_config_default['green']}
    __colors = list(__colors_config.keys())
    __color_index = 0
    __color = __colors[__color_index]
    __colors_len = len(__colors)
    __direction = 'down'

    def running(self):
        # init
        cur_color_index = self.__colors.index(self.__color)

        # change direction of color changing then reach edge of list
        if cur_color_index == 0:
            self.__direction = 'down'

        if cur_color_index + 1 == self.__colors_len:
            self.__direction = 'up'

        # change to new color
        if self.__direction == 'down':
            new_color_index = cur_color_index + 1
        else:
            new_color_index = cur_color_index - 1

        # decrease color counter
        color_counter = self.__colors_config[self.__color]
        color_counter -= 1
        self.__colors_config[self.__color] = color_counter

        # show color
        print(f'{self.__color} {color_counter + 1}...')

        # if reach color counter then reset this color counter
        if color_counter == 0:
            new_color = self.__colors[new_color_index]
            self.__colors_config[new_color] = self.__colors_config_default[new_color]
            self.__color_index = new_color_index
            self.__color = new_color


svet = TrafficLight()

while True:
    svet.running()
    time.sleep(1)
