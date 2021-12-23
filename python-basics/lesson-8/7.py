"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
 методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа)
  и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNum:
    def __init__(self, a, b):
        self.a = int(a)
        self.b = int(b)

    def __str__(self):
        return f'({self.a}, {self.b})'

    def __add__(self, other):
        res_a = self.a + other.a
        res_b = self.b + other.b
        return f'({res_a}{"+" if res_b > 0 else "-"}{res_b}j)'

    def __sub__(self, other):
        res_a = self.a - other.a
        res_b = self.b - other.b
        return f'({res_a}{"+" if res_b > 0 else "-"}{abs(res_b)}j)'


complex_1 = ComplexNum(1, 2)
complex_2 = ComplexNum(3, 4)
print(complex_1, '+', complex_2, '=', complex_1 + complex_2)
print(complex_1, '-', complex_2, '=', complex_1 - complex_2)
