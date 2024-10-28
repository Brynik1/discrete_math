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
    def RED_Q_Q():
        pass
    # Проверка сокращенного дробного на целое, если рациональное число является целым, то «да», иначе «нет»
    def INT_Q_B():
        pass
    # Преобразование целого в дробное
    def TRANS_Z_Q():
        pass
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
