from Natural import Natural
import copy


class Integer:
    def __init__(self, number: str):
        if number[0] == '-':
            self.number = list(map(int, number[1:]))
            self.sign = 1
        else:
            self.number = list(map(int, number))
            self.sign = 0

    def __str__(self):
        return ('-' if self.sign else '') + ''.join(map(str, self.number))

    # Абсолютная величина числа, результат - натуральное
    def ABS_Z_N(self):
        result = Natural(''.join(map(str, self.number)))
        return result

    # Определение положительности числа (2 - положительное, 0 — равное нулю, 1 - отрицательное)
    def POZ_Z_D(self):
        # Проверка на 0
        if self.number[0] == 0:
            return 0

        # Проверка знака
        if self.sign == 0:
            return 2
        else:
            return 1

    # Умножение целого на (-1)
    def MUL_ZM_Z(self):
        # Случай когда на входе 0
        if self.number == [0]:
            return Integer('0')

        result = Integer(str(self))

        # Меняем знак на противоположный
        if result.sign == 0:
            result.sign = 1
        else:
            result.sign = 0
        return result

    # Преобразование натурального в целое
    @staticmethod
    def TRANS_N_Z(number: Natural):
        # Копируем само число, присваиваем знак +
        result = Integer(''.join(map(str, number.number)))
        result.sign = 0
        return result

    # Преобразование целого неотрицательного в натуральное
    def TRANS_Z_N(self):
        # Преобразовываем с помощью конструктора для модуля Natural
        return Natural(''.join(map(str, self.number)))

    # Сложение целых чисел
    def ADD_ZZ_Z(self, other):

        # Выясняем знаки обоих cлагаемых
        sign_1 = self.POZ_Z_D()
        sign_2 = other.POZ_Z_D()

        # Отдельно выписываем случаи когда одно из слагаемое нулевое
        if sign_1 == 0:
            return other
        if sign_2 == 0:
            return self
        # Ветвимся по первому слагаемому, случаи когда self отрицательный
        if sign_1 == 1:
            if sign_2 == 1:  # other отрицательный
                # Превращаем self и other в натуральные, складываем их. Результат с помощью конструктора превращаем в
                # целое и меняем знак.
                return Integer(str(self.ABS_Z_N().ADD_NN_N(
                    other.ABS_Z_N()))).MUL_ZM_Z()

            # other положительный
            x1 = self.ABS_Z_N()
            x2 = other.ABS_Z_N()

            # сравниваем 2 натуральных числа
            compare = x1.COM_NN_D(x2)

            if compare == 0:  # случай когда слагаемые равны, но имеют противоположные знаки(self - отриц., other -
                # полож.)
                return Integer('0')

            if compare == 2:  # self > other
                return Integer(str(x1.SUB_NN_N(
                    x2))).MUL_ZM_Z()  # вычитаем из self other, превращаем результат в целое число и меняем знак
            return Integer(str(x2.SUB_NN_N(x1)))  # вычитаем из other self, превращаем результат в целое число
        # случаи когда self положительный
        if sign_2 == 2:  # other положительный
            return Integer(str(self.ABS_Z_N().ADD_NN_N(
                other.ABS_Z_N())))  # превращаем self и other в натуральные, складываем их. Результат с помощью
            # конструктора превращаем в целое
        # other отрицательный
        x1 = self.ABS_Z_N()
        x2 = other.ABS_Z_N()
        compare = x1.COM_NN_D(x2)
        if compare == 0:
            return Integer('0')
        if compare == 2:
            return Integer(str(x1.SUB_NN_N(x2)))
        return Integer(str(x2.SUB_NN_N(x1))).MUL_ZM_Z()

    # Вычитание целых чисел
    def SUB_ZZ_Z(self, other):

        # Производим сложение, с значением (-1) * other
        other = Integer.MUL_ZM_Z(other)
        return Integer.ADD_ZZ_Z(self, other)

    # Умножение целых чисел
    def MUL_ZZ_Z(self, other):

        # Отлавливаем 0
        if self.number == [0] or other.number == [0]:
            return Integer('0')

        # Узнаем знак итогового произведения. 1 если знаки разные, 0 если одинаковы
        mul_sign = self.sign != other.sign

        # Переводим числа в натуральные и перемножаем их
        first = Integer.TRANS_Z_N(self.ABS_Z_N())
        second = Integer.TRANS_Z_N(other.ABS_Z_N())
        result = Natural.MUL_NN_N(first, second)

        # Переводим результат в целое (пока без нужного знака)
        result = Integer.TRANS_N_Z(result)

        # Добавляем знак
        result.sign = mul_sign

        return result

    # Частное от деления целого на целое (делитель отличен от нуля)
    def DIV_ZZ_Z(self, other):

        # Проверка на ноль
        if other.number == [0]:
            raise ZeroDivisionError(f"{self.__str__()} % {other.__str__()}")

        # Ищем знак частного. 1 если знаки разные, 0 если одинаковые
        div_sign = self.sign != other.sign

        # Переводим числа в натуральные и применяем функцию деления для натуральных чисел
        first = Integer.TRANS_Z_N(self)
        second = Integer.TRANS_Z_N(other)
        result = Natural.DIV_NN_N(first, second)

        # Переводим результат в целое (пока без знака)
        result = Integer.TRANS_N_Z(result)

        # Если делимое отрицательное, то при логике выше мы можем получить отрицательный остаток
        # Чтобы избежать этого, добавим единицу к частному, если остаток отличен от нуля
        if self.sign == 1 and (Integer.ABS_Z_N(result.MUL_ZZ_Z(other)).number != self.ABS_Z_N().number):
            result = Integer.ADD_ZZ_Z(result, Integer('1'))

        # Добавление знака в ином случае
        if result.number[0] != 0:
            result.sign = div_sign

        return result

    # Остаток от деления целого на целое(делитель отличен от нуля)
    def MOD_ZZ_Z(self, other):

        # Проверка, что остаток от деления не на ноль
        if other.number == [0]:
            raise ZeroDivisionError(f"{self.__str__()} % {other.__str__()}")

        # перемножаем частное на делитель
        reducer = Integer.MUL_ZZ_Z(Integer.DIV_ZZ_Z(self, other), other)

        # Вычитаем из делимого наш reducer
        result = Integer.SUB_ZZ_Z(self, reducer)
        return result


# Тестики (нужно допилить)
def Integer_initial_test():
    print('Базовая проверка целых:')
    x = Integer('-9')
    y = Integer('-18')
    z = Natural('43')
    print(f"ABS({y}) = {y.ABS_Z_N()}")  # ABS_Z_N
    print(f"CMP({y},0) = {y.POZ_Z_D()}")  # POZ_Z_D
    print(f"{y} ∙ -1 = {y.MUL_ZM_Z()}")  # MUL_ZM_Z
    print(f'Natural({z}) → Integer({Integer.TRANS_N_Z(z)})')  # TRANS_N_Z
    print(f'Integer({y}) → Natural({y.TRANS_Z_N()})')  # TRANS_Z_N
    print(f"{x} + {y} = {x.ADD_ZZ_Z(y)}")  # ADD_ZZ_Z
    print(f"{x} - {y} = {x.SUB_ZZ_Z(y)}")  # SUB_ZZ_Z
    print(f"{x} ∙ {y} = {x.MUL_ZZ_Z(y)}")  # MUL_ZZ_Z
    print(f"{x} // {y} = {x.DIV_ZZ_Z(y)}")  # DIV_ZZ_Z
    print(f"{x} % {y} = {x.MOD_ZZ_Z(y)}")  # MOD_ZZ_Z


if __name__ == '__main__':
    Integer_initial_test()