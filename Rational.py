from Integer import Integer
from Natural import Natural


'''При написании кода обратите внимание на то, какие методы должны использоваться в реализации ваших методов (по табличке)'''
class Rational(Integer, Natural):
    def __init__(self, number: str):
        number = number.replace('|', '/')        # чтобы a|b было эквивалентно a/b
        number = number.replace(':', '/')        # чтобы a:b было эквивалентно a/b
        if number.count('/') == 1: number1, number2 = number.split('/')
        elif number.count('/') == 0: number1, number2 = number, '1'
        else: raise ValueError("Input must be a rational number 😭")
        if number2 == '0': raise ValueError("Сan't divide by zero")
        try:
            self.numerator = Integer(number1)
            self.denominator = Natural(number2)
        except ValueError:
            raise ValueError("Input must be a rational number 😭")

    def __str__(self):
        return (str(self.numerator) + '/' + str(self.denominator))



    # Сокращение дроби
    def RED_Q_Q(self):
        p=Integer(str(self.denominator.GCF_NN_N(self.numerator.ABS_Z_N())))             #превращаем числитель в натуоальное число и ищем нод числителя и знаминателя, затем результат делаем целым
        x=Integer(str(self.denominator)).DIV_ZZ_Z(p)            #знаминатель превращаем в целое число и находим его частное от деления на нод
        result=Rational('0')
        result.denominator=x.ABS_Z_N()          #записываем результат в знаминатель
        y=self.numerator.DIV_ZZ_Z(p)            #числитель делим на нод
        result.numerator=y          #записываем результат в числитель
        return result

    # Проверка сокращенного дробного на целое, если рациональное число является целым, то «да», иначе «нет»
    def INT_Q_B(self):
        p = self.denominator.GCF_NN_N(self.numerator.ABS_Z_N())             #находим нод числителя и знаминателя
        if self.denominator.COM_NN_D(p)==0:             #сравниваем нод и знаминатель равны, если они равны, то число делится нацело
            return True
        return False


    # Преобразование целого в дробное
    def TRANS_Z_Q(self):
        result = Rational('0')
        result.denominator = Natural('1')           #заносим в знменатель 1
        result.numerator = self.numerator           #число заносим в числитель
        return result

    # Преобразование сокращенного дробного в целое (если знаменатель равен 1)
    def TRANS_Q_Z():
        pass
    # Сложение дробей
    def ADD_QQ_Q():
        pass
    # Вычитание дробей
    def SUB_QQ_Q():
        pass
    # Умножение дробей
    def MUL_QQ_Q():
        pass
    # Деление дробей (делитель отличен от нуля)
    def DIV_QQ_Q():
        pass


# Пример инициализации и вывода рационального числа
if __name__ == '__main__':
    a = Rational('-4/2')
    print(a)
    x=Rational('-6/4')
    y=Rational('5')
    d=x.RED_Q_Q()
    b=x.INT_Q_B()
    c=y.TRANS_Z_Q()
    print(x,d,b,c)