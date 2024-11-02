from Natural import Natural
import copy


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
    def POZ_Z_D(self):
        for d in self.number:
            if d != 0:  # проверяем, что число не ноль
                if self.sign == 0:
                    return 2
                else:
                    return 1
        return 0

    # Умножение целого на (-1)
    def MUL_ZM_Z(self):
        result = Integer(str(self))
        if result.sign == 0:  # меняем знак на противоположный
            result.sign = 1
        else:
            result.sign = 0
        return result

    # Преобразование натурального в целое
    @staticmethod
    def TRANS_N_Z(number: Natural, sign: int = 0):
        result = Integer(''.join(map(str, number.number)))  # копируем само число
        result.sign = 0  # устанавливаем знак по умолчанию
        return result

    # Преобразование целого неотрицательного в натуральное
    def TRANS_Z_N(self):
        #if self.sign == 1: raise ValueError("Cannot convert a negative integer to natural")
        return Natural(''.join(map(str, self.number)))  # преобразовыаем с помощью конструктора для модуля Natural

    # Сложение целых чисел
    def ADD_ZZ_Z(self, other):
        s1 = self.POZ_Z_D()  # выясняем знаки обоих логаемых
        s2 = other.POZ_Z_D()
        if s1 == 0:  # отдельно выписываем случаи когда одно из слогаемых нулевое
            return other
        if s2 == 0:
            return self
        if s1 == 1:  # ветвимся по первому слогаемому, случаи когда self отрицательный
            if s2 == 1:  # other отрицательный
                return Integer(str(self.ABS_Z_N().ADD_NN_N(
                    other.ABS_Z_N()))).MUL_ZM_Z()  # превращаем self и other в натуральные, складываем их. Результат с помощью конструктора превращаем в целое и меняем знак.
            # other положительный
            x1 = self.ABS_Z_N()
            x2 = other.ABS_Z_N()
            a = x1.COM_NN_D(x2)  # сравниваем 2 натуральных числа
            if a == 0:  # случай когда слогаемы равны, но имеют противоположные знаки(self - отриц., other - полож.)
                return Integer('0')
            if a == 2:  # self>other
                return Integer(str(x1.SUB_NN_N(
                    x2))).MUL_ZM_Z()  # вычитаем из self other, превращаем результат в целое число и меняем знак
            return Integer(str(x2.SUB_NN_N(x1)))  # вычитаем из other self, превращаем результат в целое число
        # случаи когда self положительный
        if s2 == 2:  # other положительный
            return Integer(str(self.ABS_Z_N().ADD_NN_N(
                other.ABS_Z_N())))  # превращаем self и other в натуральные, складываем их. Результат с помощью конструктора превращаем в целое
        # other отрицательный
        x1 = self.ABS_Z_N()
        x2 = other.ABS_Z_N()
        a = x1.COM_NN_D(x2)
        if a == 0:
            return Integer('0')
        if a == 2:
            return Integer(str(x1.SUB_NN_N(x2)))
        return Integer(str(x2.SUB_NN_N(x1))).MUL_ZM_Z()

    # Вычитание целых чисел
    def SUB_ZZ_Z(self, other):
        other = Integer.MUL_ZM_Z(other)
        return Integer.ADD_ZZ_Z(self, other)

    # Умножение целых чисел
    def MUL_ZZ_Z(self, other):
        mul_sign = self.sign != other.sign  # 1 если знаки разные, 0 если одинаковы
        first = Integer.TRANS_Z_N(self.ABS_Z_N())  # переводим 1 число в натуральное
        second = Integer.TRANS_Z_N(other.ABS_Z_N())  # переводим 2 число в натуральное

        result = Natural.MUL_NN_N(first, second)  # здесь находится результат перемножения двух натуральных чисел
        result = Integer.TRANS_N_Z(result)  # переводим результат в целое, добавляя знак, который должен быть
        result.sign = mul_sign
        return result

    # Частное от деления целого на целое (делитель отличен от нуля)
    def DIV_ZZ_Z(self, other):
        div_sign = self.sign != other.sign  # 1 если знаки разные, 0 если одинаковые
        first = Integer.TRANS_Z_N(self)  # переводим 1 число в натуральное
        second = Integer.TRANS_Z_N(other)  # переводим 2 число в натуральное

        result = Natural.DIV_NN_N(first, second)  # применяем функцию деления для натуральных чисел

        result = Integer.TRANS_N_Z(result)  # переводим результат в целое
        result.sign = div_sign  # Добавляем знак
        return result

    # Остаток от деления целого на целое(делитель отличен от нуля)
    def MOD_ZZ_Z(self, other):
        reducer = Integer.MUL_ZZ_Z(Integer.DIV_ZZ_Z(self, other), other)  # перемножаем частное на делитель
        result = Integer.SUB_ZZ_Z(self, reducer)  # вычитаем из делимого (частное * делитель)

        return result



# Тестики (нужно допилить)
def Integer_initial_test():
    print('Базовая проверка целых:')
    x = Integer('10')
    y = Integer('-10')
    z = Natural('10')
    print(f"ABS({y}) = {y.ABS_Z_N()}")  # ABS_Z_N
    print(f"CMP({y},0) = {y.POZ_Z_D()}")  # POZ_Z_D
    print(f"{y} * -1 = {y.MUL_ZM_Z()}")  # MUL_ZM_Z
    print(f'Natural({z}) -> Integer({Integer.TRANS_N_Z(z)})')  # TRANS_N_Z
    print(f'Integer({x}) -> Natural({x.TRANS_Z_N()})')  # TRANS_Z_N
    print(f"{x} + {y} = {x.ADD_ZZ_Z(y)}")  # ADD_ZZ_Z
    print(f"{x} - {y} = {x.SUB_ZZ_Z(y)}")  # SUB_ZZ_Z
    print(f"{x} * {y} = {x.MUL_ZZ_Z(y)}")  # MUL_ZZ_Z
    print(f"{x} // {y} = {x.DIV_ZZ_Z(y)}")  # DIV_ZZ_Z
    print(f"{x} % {y} = {x.MOD_ZZ_Z(y)}")  # MOD_ZZ_Z



if __name__ == '__main__':
    Integer_initial_test()
