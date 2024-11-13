# created by Миллер Сергей, Спиридонов Александр, Копасова Ксения 3382

from modules.Rational import Rational
from modules.Integer import Integer
from modules.Natural import Natural
import copy




class Polynomial:
    def __init__(self, polynomial: str):  # инициализация многочлена
        self.numbers = polynomial.split()
        self.coefficients = [Rational(coefficient) for coefficient in polynomial.split()]
        while len(self.coefficients) > 1 and self.coefficients[
            -1].numerator.POZ_Z_D() == 0: self.coefficients = self.coefficients[:-1]

    def __str__(self):
        def f(coefficient): return f'{coefficient.numerator}/{coefficient.denominator}' if coefficient.denominator.COM_NN_D(
            Natural('1')) else str(coefficient.numerator)

        return self.visualize_polynomial(' '.join([f(coefficient) for coefficient in self.coefficients]))

    def visualize_polynomial(self, coefficients):
        def to_superscript(n):
            superscripts = {
                '0': '⁰', '1': '¹', '2': '²', '3': '³',
                '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷',
                '8': '⁸', '9': '⁹'
            }
            return ''.join(superscripts[digit] for digit in str(n))

        coefficients = str(coefficients)
        short_space = chr(0x202F)
        numbers = coefficients.split()
        if numbers[0] != '0':
            result = numbers[0]
        else:
            result = ''
        for i in range(1, len(numbers)):
            number = numbers[i]
            if number != '0':
                if number[0] == '-':
                    result += f'{short_space}-{short_space}'
                    number = number[1:]
                elif result != '':
                    result += f'{short_space}+{short_space}'
                if number != '1': result += str(number)
                result += 'x'
                if i > 1: result += to_superscript(i)
        expression = result
        expression = expression.replace('+', f'{short_space}+{short_space}').replace('-',
                                                                                     f'{short_space}-{short_space}')
        return expression

    # Сложение многочленов
    def ADD_PP_P(self, other):
        a = copy.deepcopy(self.coefficients)  # Копируем коэффициенты первого многочлена
        b = copy.deepcopy(other.coefficients)  # Копируем коэффициенты второго многочлена
        if len(b) > len(a): # Первым слагаемым берем многочлен с наибольшей длиной
            a, b = b, a
        for i in range(min(len(a), len(b))):
            a[i] = Rational.ADD_QQ_Q(a[i], b[i])  # Складываем коэффициенты
        return Polynomial(' '.join(str(coefficient) for coefficient in a))

    # Вычитание многочленов
    def SUB_PP_P(self, other):
        b = copy.deepcopy(other.coefficients)
        for i in range(len(b)):
            b[i] = Rational(f'{b[i].numerator.MUL_ZM_Z()}/{b[i].denominator}')  # Изменяем знаки коэффициентов
        return Polynomial.ADD_PP_P(self, Polynomial(' '.join(str(coefficient) for coefficient in b)))

    # Умножение многочлена на рациональное число
    def MUL_PQ_P(self, q):
        a = copy.deepcopy(self.coefficients)  # Копируем коэффициенты self
        for i in range(len(a)):
            a[i] = Rational.MUL_QQ_Q(a[i], q)  # Домножаем каждый коэффициент на q

        return Polynomial(' '.join(str(coefficient) for coefficient in a))  # Возвращвем многочлен из коэффициентов a

    # Умножение многочлена на x^k, k-натуральное или 0
    def MUL_Pxk_P(self, k):
        a = copy.deepcopy(self.coefficients)   # Копируем коэффициенты self
        # Переводим k в число и добавляем k нулей в начало списка коэффициетов
        for i in range(int(str(k))):  # Каждый проход цикла равносилен умножению многочлена на x
            a.insert(0, Rational('0'))
        return Polynomial(' '.join(str(coefficient) for coefficient in a))

    # Старший коэффициент многочлена
    def LED_P_Q(self):
        # Если многочлен пустой выводим ошибку
        if not self.coefficients:
            raise ValueError("Polynomial has no coefficients.")

        # Просматриваем все коэффициенты многочлена, находим максимальный не равный нулю
        for i in range(len(self.coefficients) - 1, -1, -1):
            # POZ_Z_D() возвращает 0, если значание равно 0
            if self.coefficients[i].numerator.POZ_Z_D():
                return self.coefficients[i]
        # Если все коэффициенты равны 0
        raise ValueError("Polynomial has no coefficients.")

    # Степень многочлена
    def DEG_P_N(self):
        # Степень многочлена на единицу меньше длины списка коэффициентов, то есть индекс максимального элемента
        return len(self.coefficients) - 1

    # Вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей
    def FAC_P_Q(self):
        numerators = []
        denominators = []
        # В два списка записываются числители и знаменатели всех коэффициентов
        for coefficient in self.coefficients:
            # Не учитываем 0 при подсчете НОД и НОК
            # POZ_Z_D() возвращает 0, если значение = 0
            if coefficient.numerator.POZ_Z_D():
                numerators.append(coefficient.numerator.ABS_Z_N())
                denominators.append(coefficient.denominator)
        if len(numerators) == 0: return Rational('1/1')  # НОД нулей - единица
        # Поочередно берется НОД двух числителей и НОК двух знаменателей
        # В итоге общий для всех числителей НОД записывается в элемент списка по индексу 0
        # В случае знаменателей тоже самое
        for i in range(1, len(numerators)):
            for j in range(len(numerators) - i):
                numerators[j] = numerators[j].GCF_NN_N(numerators[j + 1])
                denominators[j] = denominators[j].LCM_NN_N(denominators[j + 1])
        # Возвращается число вида НОД/НОК
        return Rational(f'{numerators[0]}/{denominators[0]}')

    # Умножение многочленов
    def MUL_PP_P(self, other):
        """Умножение многочленов"""
        # Определяем степень результирующего многочлена
        result_degree = self.DEG_P_N() + other.DEG_P_N()
        # Создаем список коэффициентов результирующего многочлена
        result_coeffs = [Rational('0')] * (result_degree + 1)

        # Умножаем коэффициенты соответствующих многочленов
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result_coeffs[i + j] = Rational.ADD_QQ_Q(result_coeffs[i + j],
                                                         Rational.MUL_QQ_Q(self.coefficients[i], other.coefficients[j]))

        # Создаем новый многочлен из коэффициентов результирующего и возвращаем его
        return Polynomial(' '.join(str(coefficient) for coefficient in result_coeffs))

    # Частное от деления многочлена на многочлен при делении с остатком
    def DIV_PP_P(self, other):
        if str(other) == '0':
            raise ZeroDivisionError()
        """Частное от деления многочлена на многочлен при делении с остатком"""
        # Если степень первого многочлена меньше степени второго
        if self.DEG_P_N() < other.DEG_P_N():
            return Polynomial('0')  # Возвращаем нулевой многочлен

        # Создаем список коэффициентов для хранения частного.
        # Длина частного равна разнице степеней делимого и делителя + 1
        poly_quotient = [Rational('0')] * (self.DEG_P_N() - other.DEG_P_N() + 1)

        # Копируем многочлен (для того, чтобы не влиять на оригинальный многочлен)
        dividend = copy.deepcopy(self)

        # Деление продолжается, пока степень делимого не меньше степени делителя
        while dividend.DEG_P_N() >= other.DEG_P_N():
            quotient = dividend.LED_P_Q().DIV_QQ_Q(other.LED_P_Q())  # Находим старший коэффициент частного
            degree_diff = dividend.DEG_P_N() - other.DEG_P_N()  # Находим разницу степеней многочленов
            div_poly = other.MUL_Pxk_P(degree_diff).MUL_PQ_P(quotient)  # Умножаем делитель на x^k и умножаем на частное
            poly_quotient[degree_diff] = quotient  # Сохраняем частное
            dividend = dividend.SUB_PP_P(div_poly)  # Вычитаем из делимого

        # Создаем новый многочлен из коэффициентов частного и возвращаем его
        return Polynomial(' '.join(str(i) for i in poly_quotient))

    # Остаток от деления многочлена на многочлен при делении с остатком
    def MOD_PP_P(self, other):
        # Получаем частное от деления первого многочлена на второй
        poly_quotient = self.DIV_PP_P(other)
        # Вычисляем произведение делителя на частное и вычитаем его из делимого,
        # чтобы получить остаток от деления
        return self.SUB_PP_P(Polynomial.MUL_PP_P(poly_quotient, other))

    # НОД двух многочленов
    def GCF_PP_P(self, other):
        # Копируем многочлены (для того, чтобы не влиять на оригинальные многочлены)
        coeff_polynom_1 = copy.deepcopy(self)
        coeff_polynom_2 = copy.deepcopy(other)

        # Реализуем алгоритм Евклида для вычисления НОДа многочленов
        # Пока степень второго многочлена > 0 и его значение не равно 0
        while coeff_polynom_2.DEG_P_N() > 0 and coeff_polynom_2.numbers[0] != '0':
            # Находим остаток от деления первого многочлена на второй
            residue = coeff_polynom_1.MOD_PP_P(coeff_polynom_2)
            # Меняем местами многочлены: теперь первый многочлен = второй многочлен,
            #  а второй многочлен = остаток от деления первого многочлена на второй

            coeff_polynom_1, coeff_polynom_2 = coeff_polynom_2, residue

        # Если многочлены взаимно простые - их НОД = 1
        if coeff_polynom_2.numbers[0] != '0':
            return Polynomial('1')

        # Ищем коэф., на который можно упростить многочлен
        common_factor = coeff_polynom_1.FAC_P_Q()
        # Если коэф. не равен 1, умножаем многочлен на взаимно обратный коэф.
        if common_factor != Rational('1'):
            # Умножаем результат на полученный 1/числитель
            coeff_polynom_1 = coeff_polynom_1.MUL_PQ_P(Rational(f'1/{common_factor.numerator}'))
            # Умножаем результат на полученный знаменатель
            coeff_polynom_1 = coeff_polynom_1.MUL_PQ_P(Rational(f'{common_factor.denominator}'))

        # Возвращаем значение НОДа многочленов
        return coeff_polynom_1

    # Производная многочлена
    def DER_P_P(self):
        # Если многочлен имеет степень > 0
        if self.DEG_P_N() > 0:
            # Копируем многочлен (для того, чтобы не влиять на оригинальный многочлен)
            coeff_polynom = copy.deepcopy(self.coefficients)
            # Вычисляем новые коэф. по формуле (a*x**(k))' = a*k*x**(k-1)
            derivative = [coeff_polynom[ind].MUL_QQ_Q(Rational(str(ind))) for ind in range(1, len(coeff_polynom))]
            # Создаем новый многочлен из коэффициентов
            result = Polynomial(' '.join(str(coefficient) for coefficient in derivative))

            # Возвращаем значение производной
            return result

        # Если многочлен имеет степень 0 - является константой
        return Polynomial('0')

    # Преобразование многочлена — кратные корни в простые
    def NMP_P_P(self):
        # Копируем многочлен (для того, чтобы не влиять на оригинальный многочлен)
        polynom = copy.deepcopy(self)
        # Находим производную многочлена
        derivative = Polynomial.DER_P_P(polynom)
        # Находим НОД многочлена и его производной (если существует производная)
        if derivative:
            gcd_polynomial = Polynomial.GCF_PP_P(polynom, derivative)
        else:
            # Если производной не существует, то НОД многочлена = многочлену
            gcd_polynomial = polynom

        # Находим частное от многочлена при делении на его НОД (если НОД != 1)
        if str(gcd_polynomial) != '1':
            simple_polynomial = Polynomial.DIV_PP_P(polynom, gcd_polynomial)
        else:
            # Иначе частное равно самому многочлену
            simple_polynomial = polynom

        # Возвращаем значение упрощеного многочлена
        return simple_polynomial


# Тестики (базовая демонстрация работы)
def Polynomial_initial_test():
    print('Базовая проверка многочленов:')
    x = Polynomial('2 1/2 4 -3 1')
    y = Polynomial('1 1 22 2 2 2 -2/5')
    z = Rational('2')
    k = Natural('3')
    print(f'({x}) + ({y})  =  {Polynomial.ADD_PP_P(x, y)}')  # ADD_PP_P
    print(f'({x}) - ({y})  =  {Polynomial.SUB_PP_P(x, y)}')  # SUB_PP_P
    print(f'({x}) ∙ {z}  =  {Polynomial.MUL_PQ_P(x, z)}')  # MUL_PQ_P
    print(f'({x}) ∙ x^{k}  =  {Polynomial.MUL_Pxk_P(x, k)}')  # MUL_Pxk_P
    print(f'Старший коэффициент {x}  =  {Polynomial.LED_P_Q(x)}')  # LED_P_Q
    print(f'DEG {x} = {Polynomial.DEG_P_N(x)}')  # DEG_P_N
    print(f'НОД/НОК {x}  =  {Polynomial.FAC_P_Q(x)}')  # FAC_P_Q
    print(f'({x}) ∙ ({y})  =  {Polynomial.MUL_PP_P(x, y)}')  # MUL_PP_P
    print(f'({x}) // ({y})  =  {Polynomial.DIV_PP_P(x, y)}')  # DIV_PP_P
    print(f'{x}  %  {y}  =  {Polynomial.MOD_PP_P(x, y)}')       # MOD_PP_P
    print(f'НОД  ({x};  {y})  =  {Polynomial.GCF_PP_P(y, x)}')  # GCF_PP_P
    print(f'Производная {x}  =  {Polynomial.DER_P_P(x)}')  # DER_P_P
    print(f'NMP ({x})  =  {Polynomial.NMP_P_P(x)}')             # NMP_P_P
