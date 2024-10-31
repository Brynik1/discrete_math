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

    def __mul__(self, other):
        # Для добавления других методов умножения можно дополнять этот
        if type(other) == Polynomial:
            coeff_len = len(other.coefficients)
            mul_coeffs = []
            for i in range(coeff_len):
                mul_coeffs.append(self.MUL_PQ_P(other.coefficients[i]).MUL_Pxk_P(coeff_len-i))
                if i != 0:
                    mul_coeffs[0].ADD_PP_P(mul_coeffs[i])

            self.coefficients = mul_coeffs[0]
            return self

    def __floordiv__(self, other):
        # Есть возможность определить остальное деление через этот же метод
        if type(other) == Polynomial:
            # Определение частного от деления полинома на полином
            poly_quotient = [0]*(self.DEG_P_N() + 1)
            # Копирование значений коэффициентов
            # dividend - делимое
            dividend = Polynomial('')
            dividend.coefficients = [x for x in self.coefficients]

            # Деление происходит пока степень делимого не будет меньше делителя
            # Алгоритм как при делении столбиком
            while dividend.DEG_P_N() >= other.DEG_P_N():
                # Quotient - частное, в данном случае от деления коэффициентов
                quotient = dividend.LED_P_Q().DIV_QQ_Q(other.LED_P_Q())

                # Умножение на x^k, для уравнения степеней, умножение на частное от деления коэффициентов
                div_poly = other.MUL_Pxk_P(dividend.DEG_P_N() - other.DEG_P_N()).MUL_PQ_P(quotient)

                poly_quotient[dividend.DEG_P_N() - other.DEG_P_N()] = quotient

                dividend = dividend.SUB_PP_P(div_poly)

            result = Polynomial('')
            result.coefficients = poly_quotient
            return result

    def __mod__(self, other):
        if type(other) == Polynomial:
            # Находим частное от деления
            # Умножаем на делитель и потом вычитатем
            poly_quotient = self // other
            poly_quotient *= other

            return self.SUB_PP_P(poly_quotient)

    # Сложение многочленов
    def ADD_PP_P(self, other):
        pass
    # Вычитание многочленов
    def SUB_PP_P(self, other):
        pass
    # Умножение многочлена на рациональное число
    def MUL_PQ_P(self, rational):
        pass
    # Умножение многочлена на x^k, k-натуральное или 0
    def MUL_Pxk_P(self):
        pass
    # Старший коэффициент многочлена
    def LED_P_Q(self):
        pass
    # Степень многочлена
    def DEG_P_N(self):
        while self.coefficients[0] == 0:
            self.coefficients.pop(0)
        return len(self.coefficients) - 1

    # Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей
    def FAC_P_Q(self):
        numerators = []
        denominators = []

        # В два списка записываются числители и знаменатели всех коэффициентов
        for coefficient in self.coefficients:
            numerators.append(coefficient.numerator.ABS_Z_N().TRANS_Z_N())
            denominators.append(coefficient.denominator)

        # Поосередно берется НОД двух числителей и НОК двух знаминателей
        # В итоге общий для всех числитеоей НОД записывается в 0 элемент списка
        # В случае знаменателей тоже самое
        for i in range(1, len(numerators)):
            for j in range(len(numenators) - i):
                numerators[j] = numerators[j].GCF_NN_N(numerators[j + 1])
                denominators[j] = denominators[j].LCM_NN_N(denominators[j + 1])

        # Возвращается число вида НОД/НОК
        return Rational(f'{numerators[0].TRANS_N_Z()}/{denominators[0]}')

    # Умножение многочленов
    def MUL_PP_P(self, other):
        # Умножение определено в магическом методе
        # Но здесь тоже будет =)
        return self * other

    # Частное от деления многочлена на многочлен при делении с остатком
    def DIV_PP_P(self, other):
        # Деление определено в магическом методе
        # Но здесь тоже будет :D
        return self // other

    # Остаток от деления многочлена на многочлен при делении с остатком
    def MOD_PP_P(self, other):
        # Получение остатка от деления реальзовано в виде операции взятия остатка, с помощью магического метода
        return self % other

    # НОД многочленов
    def GCF_PP_P(self):
        pass
    # Производная многочлена
    def DER_P_P(self):
        pass
    # Преобразование многочлена — кратные корни в простые
    def NMR_P_P(self):
        pass


# Пример инициализации и вывода многочлена
if __name__ == '__main__':
    a = Polynomial('-2/3 3 4 -2')   #    -2/3  +  3X + 4X^2 - 2X^3
    print(a)

