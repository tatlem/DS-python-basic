# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def showData(name, surname,birth,city_of_residence,email,phone):
    print(f'name: {name}; surname:{surname}; birth: {birth}; city_of_residence: {city_of_residence}; email: {email}; phone: {phone}')


showData(name='Roman',surname='Goncharenya',birth='April',city_of_residence='Nizhnevartovsk',email='goncharenya@gmail.com',phone='+7-921-123-45-67')