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
    def MUL_ZM_Z():
        pass
    # Преобразование натурального в целое
    def TRANS_N_Z():
        pass
    # Преобразование целого неотрицательного в натуральное
    def TRANS_Z_N():
        pass
    # Сложение целых чисел
    def ADD_ZZ_Z():
        pass
    # Вычитание целых чисел
    def SUB_ZZ_Z():
        pass
    # Умножение целых чисел
    def MUL_ZZ_Z():
        pass
    # Частное от деления целого на целое (делитель отличен от нуля)
    def MUL_ZZ_Z():
        pass
    # Остаток от деления целого на целое(делитель отличен от нуля)
    def DIV_ZZ_Z():
        pass


# Пример инициализации и вывода целого числа
if __name__ == '__main__':
    a = Integer('-100')
    print(a)
