from Rational import Rational


'''При написании кода обратите внимание на то, какие методы должны использоваться в реализации ваших методов (по табличке)'''
class Polynomial(Rational):
    def __init__(self, polynomial: str):
        self.numbers = polynomial.split()
        try:
            self.coefficients = [Rational(coefficient) for coefficient in polynomial.split()]
        except ValueError:
            raise ValueError("Input must be a polynomial 😭")

    def __str__(self):
        return ' '.join([str(coefficient) for coefficient in self.coefficients])



    # Сложение многочленов
    def ADD_PP_P():
        pass
    # Вычитание многочленов
    def SUB_PP_P():
        pass
    # Умножение многочлена на рациональное число
    def MUL_PQ_P():
        pass
    # Умножение многочлена на x^k, k-натуральное или 0
    def MUL_Pxk_P():
        pass
    # Старший коэффициент многочлена
    def LED_P_Q():
        pass
    # Степень многочлена
    def DEG_P_N():
        pass
    # Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей
    def FAC_P_Q():
        pass
    # Умножение многочленов
    def MUL_PP_P():
        pass
    # Частное от деления многочлена на многочлен при делении с остатком
    def DIV_PP_P():
        pass
    # Остаток от деления многочлена на многочлен при делении с остатком
    def MOD_PP_P():
        pass
    # НОД многочленов
    def GCF_PP_P():
        pass
    # Производная многочлена
    def DER_P_P():
        pass
    # Преобразование многочлена — кратные корни в простые
    def NMR_P_P():
        pass


# Пример инициализации и вывода многочлена
if __name__ == '__main__':
    a = Polynomial('-2/3 3 4 -2')   #    -2/3  +  3X + 4X^2 - 2X^3
    print(a)

