from Integer import Integer
from Natural import Natural


class Rational:
    def __init__(self, number: str):
        number = number.replace('|', '/')        # чтобы a|b было эквивалентно a/b
        number = number.replace(':', '/')        # чтобы a:b было эквивалентно a/b
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
        if self.numerator.POZ_Z_D() == 0:
            return Rational('0/1')
        p = Integer(str(self.denominator.GCF_NN_N(self.numerator.ABS_Z_N())))  # превращаем числитель в натуоальное число и ищем нод числителя и знаминателя, затем результат делаем целым
        x = Integer(str(self.denominator)).DIV_ZZ_Z(p)  # знаменатель превращаем в целое число и делим на нод
        y = self.numerator.DIV_ZZ_Z(p)  # числитель делим на нод
        result = Rational('0')
        result.denominator=x.ABS_Z_N()  # записываем результат в знаменатель
        result.numerator=y          # записываем результат в числитель
        return result

    # Проверка сокращенного дробного на целое, если рациональное число является целым, то «да», иначе «нет»
    def INT_Q_B(self):
        p = self.denominator.GCF_NN_N(self.numerator.ABS_Z_N())  # находим нод числителя и знаминателя
        if self.denominator.COM_NN_D(p)==0:  # сравниваем нод и знаминатель равны, если они равны, то число делится нацело
            return True
        return False


    # Преобразование целого в дробное
    @staticmethod
    def TRANS_Z_Q(number: Integer):
        result = Rational(f'{number}/1')
        return result

    # Преобразование сокращенного дробного в целое (если знаменатель равен 1)
    def TRANS_Q_Z(self):
        return Integer(str(self.numerator))

    # Сложение дробей
    def ADD_QQ_Q(self, other):
        new_numerator = Integer.ADD_ZZ_Z(Integer.MUL_ZZ_Z(self.numerator,
                                                          Integer.TRANS_N_Z(other.denominator)),
                                         Integer.MUL_ZZ_Z(Integer.TRANS_N_Z(self.denominator),
                                                          other.numerator))  # новый числитель
        new_denominator = Integer.MUL_ZZ_Z(Integer.TRANS_N_Z(self.denominator),
                                           Integer.TRANS_N_Z(other.denominator))  # новый знаменатель
        result = Rational(f'{new_numerator}/{new_denominator}')
        return result.RED_Q_Q()


    # Вычитание дробей
    def SUB_QQ_Q(self, other):
        new_other = Rational(f'{other.numerator.MUL_ZM_Z()}/{other.denominator}')
        return self.ADD_QQ_Q(new_other)

    # Умножение дробей
    def MUL_QQ_Q(self, other):
        new_numerator = Integer.MUL_ZZ_Z(self.numerator, other.numerator)  # новый числитель
        new_denominator = Natural.MUL_NN_N(self.denominator, other.denominator)  # новый знаменатель
        result = Rational(f'{new_numerator}/{new_denominator}')
        return result.RED_Q_Q()

    # Деление дробей (делитель отличен от нуля)
    def DIV_QQ_Q(self, other):
        new_numerator = Integer.TRANS_N_Z(other.denominator)  # Переворачиваем дроби
        new_sign = 1 if other.numerator.POZ_Z_D() == 1 else 0  # Сохраняем знак перевернутой дроби
        if new_sign:
            new_numerator = new_numerator.MUL_ZM_Z()  # Переносим знак в числитель
        new_denominator = other.numerator.TRANS_Z_N() # чтобы далее произвести умножение
        new_other = Rational(f'{new_numerator}/{new_denominator}')

        return Rational.MUL_QQ_Q(self, new_other)  # Умножаем дробь на перевернутую



# Тестики (нужно допилить)
def Rational_initial_test():
    print('Базовая проверка рациональных:')
    x = Rational('-3/2')
    y = Rational('-6/3')
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


def is_Natural(number):
    return (number != '' and (type(number) == str) and all(c.isdigit() for c in number))
def is_Integer(number):
    if number != '' and type(number) == str:
        if number[0] == '-': return (len(number) > 1) and is_Natural(number[1:])
        else: return is_Natural(number)
    else: return False
def is_Rational(number):
    if number.count('/') > 1: return False
    elif number.count('/') == 1: num1, num2 = number.split('/')
    else: num1, num2 = number, '1'
    return is_Integer(num1) and is_Natural(num2) and num2 != '0'
if __name__ == '__main__':
    Rational_initial_test()
