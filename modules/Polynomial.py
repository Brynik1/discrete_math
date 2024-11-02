from Rational import Rational
from Integer import Integer
from Natural import Natural
import copy


'''    
    Найти и исправить
    
    У функции деления с остатком результат верный, но очень долгие вычисления!
    
    Пример (считается дольше пяти минут):
    x = Polynomial('-35/1 -33/1 -62/1 22/1')
    y = Polynomial('207/121 51/22 1207/242')
    print(f'{x}  %  {y}  =  {Polynomial.MOD_PP_P(x, y)}')
    
    Ps: можно менять другие функции, если нужно
'''


class Polynomial:
    def __init__(self, polynomial: str):  # инициализация многочлена
        self.numbers = polynomial.split()
        try:
            self.coefficients = [Rational(coefficient) for coefficient in polynomial.split()]
            while len(self.coefficients) > 1 and self.coefficients[-1].numerator.POZ_Z_D() == 0: self.coefficients = self.coefficients[:-1]
        except ValueError:
            raise ValueError("Input must be a polynomial 😭")

    def __str__(self):
        def f(coefficient): return f'{coefficient.numerator}/{coefficient.denominator}' if coefficient.denominator.COM_NN_D(Natural('1')) else str(coefficient.numerator)
        return ' '.join([f(coefficient) for coefficient in self.coefficients])

    # Сложение многочленов
    def ADD_PP_P(self, oth):
        a = copy.deepcopy(self.coefficients)  # Копируем коэффициенты первого многочлена
        b = copy.deepcopy(oth.coefficients)  # Копируем коэффициенты второго многочлена
        if len(b) > len(a): a, b = b, a  # Первым слагаемым берем многочлен с наибольшей длиной
        for i in range(min(len(a), len(b))):
            a[i] = Rational.ADD_QQ_Q(a[i], b[i])  # Складываем коэффициенты
        return Polynomial(' '.join(str(coefficient) for coefficient in a))

    # Вычитание многочленов
    def SUB_PP_P(self, oth):
        b = copy.deepcopy(oth.coefficients)
        for i in range(len(b)):
            b[i] = Rational(f'{b[i].numerator.MUL_ZM_Z()}/{b[i].denominator}')  # Изменяем знаки коэффициентов
        return Polynomial.ADD_PP_P(self, Polynomial(' '.join(str(coefficient) for coefficient in b)))


    # Умножение многочлена на рациональное число
    def MUL_PQ_P(self, q):
        a = copy.deepcopy(self.coefficients)
        for i in range(len(a)):
            a[i] = Rational.MUL_QQ_Q(a[i], q)
        return Polynomial(' '.join(str(coefficient) for coefficient in a))

    # Умножение многочлена на x^k, k-натуральное или 0
    def MUL_Pxk_P(self, k):
        a = copy.deepcopy(self.coefficients)
        for i in range(int(str(k))):
            a.insert(0, Rational('0'))
        return Polynomial(' '.join(str(coefficient) for coefficient in a))

    # Старший коэффициент многочлена
    def LED_P_Q(self):
        # Возвращаем старший коэффициент, наверное не нулевой, правда,я надеюсь
        # Возвращаем <object Rational>
        if not self.coefficients:
            raise ValueError("Polynomial has no coefficients.")
        for i in range(len(self.coefficients) - 1, 0, -1):
            if self.coefficients[-1].numerator.POZ_Z_D() != 0:
                return self.coefficients[-1]

    # Степень многочлена
    def DEG_P_N(self):
        return len(self.coefficients) - 1


    # Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей
    def FAC_P_Q(self):
        numerators = []
        denominators = []
        # В два списка записываются числители и знаменатели всех коэффициентов
        for coefficient in self.coefficients:
            numerators.append(coefficient.numerator.ABS_Z_N())
            denominators.append(coefficient.denominator)
        # Поочередно берется НОД двух числителей и НОК двух знаменателей
        # В итоге общий для всех числителей НОД записывается в 0 элемент списка
        # В случае знаменателей тоже самое
        for i in range(1, len(numerators)):
            for j in range(len(numerators) - i):
                numerators[j] = numerators[j].GCF_NN_N(numerators[j + 1])
                denominators[j] = denominators[j].LCM_NN_N(denominators[j + 1])
        # Возвращается число вида НОД/НОК
        return Rational(f'{numerators[0]}/{denominators[0]}')


    # Умножение многочленов
    def MUL_PP_P(self, other):
        # Определяем степень результирующего многочлена
        result_degree = self.DEG_P_N() + other.DEG_P_N()
        result_coeffs = [Rational('0')] * (result_degree + 1)

        # Умножаем коэффициенты
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result_coeffs[i+j] = Rational.ADD_QQ_Q(result_coeffs[i+j], Rational.MUL_QQ_Q(self.coefficients[i], other.coefficients[j]))

        return Polynomial(' '.join(str(coefficient) for coefficient in result_coeffs))

    # Частное от деления многочлена на многочлен при делении с остатком
    def DIV_PP_P(self, other):
        if self.DEG_P_N() < other.DEG_P_N():
            return Polynomial('0')  # Возвращаем нулевой многочлен
        poly_quotient = [Rational('0')] * (self.DEG_P_N() - other.DEG_P_N() + 1)
        dividend = copy.deepcopy(self)  # Копируем

        # Деление продолжается, пока степень делимого не меньше степени делителя
        while dividend.DEG_P_N() >= other.DEG_P_N():
            quotient = dividend.LED_P_Q().DIV_QQ_Q(other.LED_P_Q())  # Находим старший коэффициент частного
            degree_diff = dividend.DEG_P_N() - other.DEG_P_N()
            div_poly = other.MUL_Pxk_P(degree_diff).MUL_PQ_P(quotient)  # Умножаем делитель на x^k и умножаем на частное
            poly_quotient[degree_diff] = quotient  # Сохраняем частное
            dividend = dividend.SUB_PP_P(div_poly)  # Вычитаем из делимого

        # Создаем новый многочлен из коэффициентов частного
        return Polynomial(' '.join(str(i) for i in poly_quotient))

    # Остаток от деления многочлена на многочлен при делении с остатком
    def MOD_PP_P(self, other):
        poly_quotient = self.DIV_PP_P(other)
        return self.SUB_PP_P(Polynomial.MUL_PP_P(poly_quotient, other))

    # НОД многочленов
    def GCF_PP_P(self, other):
        """Нахождение НОД многочленов с использованием алгоритма Евклида."""
        a = copy.deepcopy(self)
        b = copy.deepcopy(other)

        # Алгоритм Евклида для нахождения НОД
        while b.DEG_P_N() > 0 and b != Polynomial('0'):
            a, b = b, a.MOD_PP_P(b)  # Обновляем a и b

        return a

    # Производная многочлена
    def DER_P_P(self):
        coeff_polynom = copy.deepcopy(self.coefficients)
        # вычисляем новые коэф. по формуле (a*x**(k))' = a*k*x**(k-1)
        derivative = [coeff_polynom[ind].MUL_QQ_Q(Rational(str(ind))) for ind in range(1, len(coeff_polynom))]
        # Создаем новый многочлен из коэффициентов
        result = Polynomial(' '.join(str(coefficient) for coefficient in derivative))
        return result

    # Преобразование многочлена — кратные корни в простые
    def NMP_P_P(self):
        # Находим производную многочлена
        polynom = copy.deepcopy(self)
        derivative = Polynomial.DER_P_P(polynom)
        # Находим НОД многочлена и его производной
        gcd_polynomial = Polynomial.GCF_PP_P(polynom, derivative)
        # Находим частное от многочлена при делении на его НОД
        simple_polynomial = Polynomial.DIV_PP_P(polynom, gcd_polynomial)
        return simple_polynomial



# Тестики (нужно допилить)
def Polynomial_initial_test():
    print('Базовая проверка многочленов:')
    x = Polynomial('2 1/2 4 -3 1')
    y = Polynomial('1 1 22 2 2 2 -2/5')
    z = Rational('2')
    k = Natural('3')
    print(f'({x})  +  ({y})  =  {Polynomial.ADD_PP_P(x, y)}')  # ADD_PP_P
    print(f'({x})  -  ({y})  =  {Polynomial.SUB_PP_P(x, y)}')  # SUB_PP_P
    print(f'({x})  *  {z}  =  {Polynomial.MUL_PQ_P(x, z)}')  # MUL_PQ_P
    print(f'({x})  *  x^{k}  =  {Polynomial.MUL_Pxk_P(x, k)}')  # MUL_Pxk_P
    print(f'Старший коэффициент ({x})  =  {Polynomial.LED_P_Q(x)}')  # LED_P_Q
    print(f'DEG ({x})  =  {Polynomial.DEG_P_N(x)}')  # DEG_P_N
    print(f'НОД/НОК ({x})  =  {Polynomial.FAC_P_Q(x)}')  # FAC_P_Q
    print(f'{x}  *  {y}  =  {Polynomial.MUL_PP_P(x, y)}')  # MUL_PP_P
    print(f'{x}  //  {y}  =  {Polynomial.DIV_PP_P(x, y)}')  # DIV_PP_P
    # print(f'{x}  %  {y}  =  {Polynomial.MOD_PP_P(x, y)}')       # MOD_PP_P
    # print(f'НОД  ({x};  {y})  =  {Polynomial.GCF_PP_P(y, x)}')  # GCF_PP_P
    print(f'Производная ({x})  =  {Polynomial.DER_P_P(x)}')  # DER_P_P
    # print(f'NMP ({x})  =  {Polynomial.NMP_P_P(x)}')             # NMP_P_P



if __name__ == '__main__':
    Polynomial_initial_test()
