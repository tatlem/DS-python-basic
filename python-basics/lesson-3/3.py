# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    numbers = [a, b, c]
    numbers_sorted = sorted(numbers)

    return numbers_sorted[1] + numbers_sorted[2]

print(my_func(3, 5, 2))
