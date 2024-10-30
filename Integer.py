from Natural import Natural


'''При написании кода обратите внимание на то, какие методы должны использоваться в реализации ваших методов (по табличке)'''
class Integer(Natural):
    def __init__(self, number: str):
        if not self.validate_Integer(number):
            raise ValueError("Input must be a integers number 😭")

        if number[0] == '-':
            self.number = list(map(int, number[1:]))
            self.sign = 1
        else:
            self.number = list(map(int, number))
            self.sign = 0

    @staticmethod
    def validate_Integer(number: str):
        return all(c.isdigit() for c in number[1:]) and (number[0].isdigit() or number[0] == '-')

    def __str__(self):
        return ('-' if self.sign else '') + ''.join(map(str, self.number))


    # Абсолютная величина числа, результат - натуральное
    def ABS_Z_N(self):
        result = Natural(''.join(map(str, self.number)))
        return result

    # Определение положительности числа (2 - положительное, 0 — равное нулю, 1 - отрицательное)
    def POZ_Z_D():
        pass

    # Умножение целого на (-1)
    def MUL_ZM_Z(self):
        prev_sign = self.sign
        self.sign = 0 if prev_sign else 1
        return self

    # Преобразование натурального в целое
    def TRANS_N_Z(self, sign: int = 0):

        return Integer(f'{"-" if sign else ""}'+''.join([str(i) for i in self.number]))

    # Преобразование целого неотрицательного в натуральное
    def TRANS_Z_N(self):
        return Natural(''.join([str(i) for i in self.number]))
        pass

    # Сложение целых чисел
    def ADD_ZZ_Z():
        pass

    # Вычитание целых чисел
    def SUB_ZZ_Z(self, other):
        other = Integer.MUL_ZM_Z(other)
        return Integer.ADD_ZZ_Z(self, other)

    # Умножение целых чисел
    def MUL_ZZ_Z(self, other):
        mul_sign = self.sign != other.sign  # 1 если знаки разные, 0 если одинаковые
        first = Integer.TRANS_Z_N(self)  # переводим 1 число в натуральное
        second = Integer.TRANS_Z_N(other)  # переводим 2 число в натуральное

        result = Natural.MUL_NN_N(first, second)  # здесь находится результат перемножения двух натуральных чисел

        return Integer.TRANS_N_Z(result, sign=mul_sign)  # переводим результат в целое, добавляя знак, который должен быть

    # Частное от деления целого на целое (делитель отличен от нуля)
    def DIV_ZZ_Z(self, other):
        div_sign = self.sign != other.sign  # 1 если знаки разные, 0 если одинаковые
        first = Integer.TRANS_Z_N(self)  # переводим 1 число в натуральное
        second = Integer.TRANS_Z_N(other)  # переводим 2 число в натуральное

        result = Natural.DIV_NN_N(first, second)  # применяем функцию деления для натуральных чисел

        return Integer.TRANS_N_Z(result, sign=div_sign)  # переводим результат в целое, добавляя знак

    # Остаток от деления целого на целое(делитель отличен от нуля)
    def MOD_ZZ_Z(self, other):
        reducer = Integer.MUL_ZZ_Z(Integer.DIV_ZZ_Z(self, other), other)  # перемножаем частное на делитель
        result = Integer.SUB_ZZ_Z(self, reducer)  # вычитаем из делимого (частное * делитель)

        return result


if __name__ == '__main__':
    a = Integer('100')
    b = Integer('15')
    print(Integer.MUL_ZZ_Z(a,b))
    print(Integer.DIV_ZZ_Z(a, b))
    print(Integer.MUL_ZM_Z(a))
