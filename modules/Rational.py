from Integer import Integer
from Natural import Natural


class Rational:
    def __init__(self, number: str):
        number = number.replace('|', '/').replace(':', '/')
        if number.count('/') == 1: number1, number2 = number.split('/')
        elif number.count('/') == 0: number1, number2 = number, '1'
        self.numerator = Integer(number1)
        self.denominator = Natural(number2) if self.numerator.POZ_Z_D() != 0 else Natural('1')

    def __str__(self):
        if Natural.COM_NN_D(self.denominator,Natural('1')) == 0:
            return str(self.numerator)
        return f'{self.numerator}/{self.denominator}'



    # Сокращение дроби
    def RED_Q_Q(self):
        if self.numerator.POZ_Z_D() == 0: return Rational('0')
        p = Integer(str(self.denominator.GCF_NN_N(self.numerator.ABS_Z_N())))  # Находим НОД числителя и знаменателя
        # Сокращаем числитель и знаменатель
        new_denominator = Integer(str(self.denominator)).DIV_ZZ_Z(p).ABS_Z_N()  # Записываем знаменатель
        new_numerator = self.numerator.DIV_ZZ_Z(p)  # Записываем числитель
        result = Rational(f'{new_numerator}/{new_denominator}')
        return result

    # Проверка сокращенного дробного на целое, если рациональное число является целым, то «да», иначе «нет»
    def INT_Q_B(self):
        p = self.denominator.GCF_NN_N(self.numerator.ABS_Z_N())  # находим нод числителя и знаменателя
        # числитель равен нулю or нод равен знаменателю => целое
        return self.numerator.POZ_Z_D() == 0 or self.denominator.COM_NN_D(p) == 0


    # Преобразование целого в дробное
    @staticmethod
    def TRANS_Z_Q(number: Integer):
        return Rational(f'{number}/1')  # преобразование через конструктор

    # Преобразование сокращенного дробного в целое (если знаменатель равен 1)
    def TRANS_Q_Z(self):
        return Integer(str(self.numerator))  # преобразование через конструктор

    # Сложение дробей
    def ADD_QQ_Q(self, other):
        # Вычисляем новый числитель: Числитель первой дроби умножаем на знаменатель второй дроби
        # и добавляем к нему числитель второй дроби, умноженный на знаменатель первой дроби.
        new_numerator = Integer.ADD_ZZ_Z(
            Integer.MUL_ZZ_Z(self.numerator, Integer.TRANS_N_Z(other.denominator)),
            Integer.MUL_ZZ_Z(Integer.TRANS_N_Z(self.denominator), other.numerator)
        )

        # Вычисляем новый знаменатель: Умножаем знаменатели обеих дробей
        new_denominator = Integer.MUL_ZZ_Z(
            Integer.TRANS_N_Z(self.denominator),  # Знаменатель первой дроби
            Integer.TRANS_N_Z(other.denominator)  # Знаменатель второй дроби
        )
        result = Rational(f'{new_numerator}/{new_denominator}')  # Формируем дробь из числителя и знаменателя
        return result.RED_Q_Q()  # Возвращаем сокращенную дробь


    # Вычитание дробей
    def SUB_QQ_Q(self, other):
        new_other = Rational(f'{other.numerator.MUL_ZM_Z()}/{other.denominator}')  # меняем знак второй дроби
        return self.ADD_QQ_Q(new_other)  # складываем дроби

    # Умножение дробей
    def MUL_QQ_Q(self, other):
        new_numerator = Integer.MUL_ZZ_Z(self.numerator, other.numerator)  # новый числитель
        new_denominator = Natural.MUL_NN_N(self.denominator, other.denominator)  # новый знаменатель
        result = Rational(f'{new_numerator}/{new_denominator}')  # формируем результат
        return result.RED_Q_Q()  # возвращаем сокращенный результат

    # Деление дробей (делитель отличен от нуля)
    def DIV_QQ_Q(self, other):
        new_numerator = Integer.TRANS_N_Z(other.denominator)  # Переворачиваем дроби
        new_sign = 1 if other.numerator.POZ_Z_D() == 1 else 0  # Сохраняем знак перевернутой дроби
        if new_sign:
            new_numerator = new_numerator.MUL_ZM_Z()  # Переносим знак в числитель для умножения
        new_denominator = other.numerator.TRANS_Z_N()
        new_other = Rational(f'{new_numerator}/{new_denominator}')

        return Rational.MUL_QQ_Q(self, new_other)  # Умножаем дробь на перевернутую



# Тестики (нужно допилить)
def Rational_initial_test():
    print('Базовая проверка рациональных:')
    x = Rational('-6/2')
    y = Rational('-6/4')
    z = Integer('-10')
    print(f'{x} = {x.RED_Q_Q()}')  # RED_Q_Q
    print(f'{x} is int = {x.INT_Q_B()}')  # INT_Q_B
    print(f'{y} is int = {y.INT_Q_B()}')  # INT_Q_B
    print(f'Integer({z}) → Rational({Rational.TRANS_Z_Q(z)})')  # TRANS_Z_Q
    print(f'Rational({y}) → Integer({y.TRANS_Q_Z()})')  # TRANS_Q_Z
    print(f'{x} + {y} = {x.ADD_QQ_Q(y)}')  # ADD_QQ_Q
    print(f'{x} - {y} = {x.SUB_QQ_Q(y)}')  # SUB_QQ_Q
    print(f'{x} ∙ {y} = {x.MUL_QQ_Q(y)}')  # MUL_QQ_Q
    print(f'{x} / {y} = {x.DIV_QQ_Q(y)}')  # DIV_QQ_Q



if __name__ == '__main__':
    Rational_initial_test()
