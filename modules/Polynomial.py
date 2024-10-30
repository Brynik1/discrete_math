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
        pass# НОД многочленов
    def GCD_PP_P(self, coeff_polynom_1: list, coeff_polynom_2: list) -> list:
        """Нахождение НОДа многочленов"""

        def compare_polinomials(self, coeff_polynom_1: list, coeff_polynom_2: list):
            """Сравнение двух многочленов"""
            # убираем нули для правильного сравнения многочленов
            while any(coeff_polynom_1) == False and coeff_polynom_1[0] == 0:
                coeff_polynom_1.pop(0)
        
            while any(coeff_polynom_2) == False and coeff_polynom_2[0] == 0:
                coeff_polynom_2.pop(0)

            # сравниваем степени многочленов DEG_P_N
            if self.DEG_P_N(coeff_polynom_1) > self.DEG_P_N(coeff_polynom_2):
                return 1
            elif self.DEG_P_N(coeff_polynom_1) < self.DEG_P_N(coeff_polynom_2):
                return 2
            
            counter1, counter2 = 0, 0
            # если степени одинаковые, то сравниваем коэфф. по порядку
            for coeff1, coeff2 in zip(coeff_polynom_1, coeff_polynom_2):
                if coeff1 > coeff2:
                    counter1 += 1
                elif coeff2 > coeff1:
                    counter2 += 1
            if counter1 > counter2:
                return 1 # коэфф. у первого многочлена больше
            elif counter2 > counter1:
                return 2 # коэфф. у второго многочлена больше
            else:
                return 0 # многочлены одинаковые

        while any(coeff_polynom_2): # проверяем, есть ли ненулевые коэф.
            # сравниваем многочлены
            # если второй больше первого, меняем их местами для удобства вычислений
            if compare_polinomials(coeff_polynom_1, coeff_polynom_2) == 2: 
                coeff_polynom_1, coeff_polynom_2 = coeff_polynom_2, coeff_polynom_1
            # если многочлены равны, то сразу возвращаем НОД
            elif compare_polinomials(coeff_polynom_1, coeff_polynom_2) == 0:
                return coeff_polynom_1
            
            # делим многочлены и находим остаток 
            residue = MOD_PP_P(coeff_polynom_1, coeff_polynom_2)
            # обновляем значение coeff_polynom_1 и coeff_polynom_2 
            coeff_polynom_1, coeff_polynom_2 = coeff_polynom_2, residue

        # Убираем возможные ведущие нули
        while coeff_polynom_1 and abs(coeff_polynom_1[0]) == 0:
            coeff_polynom_1.pop(0)

        return coeff_polynom_1

    # Производная многочлена
    def DER_P_P(self, coeff_polynom: list) -> list:
        """Нахождение производной многочлена"""
        derivative = [] # массив коэф. производной многочлена
        coeff_polynom.reverse() # переворачиваем массив для удобства вычисления
        # вычисляем новые коэф. по формуле (a*x**(k))' = a*k*x**(k-1)
        derivative = [coeff_polynom[ind]*ind for ind in range(1, len(coeff_polynom))] 
        derivative.reverse() # переворачиваем полученный массив

        return derivative if derivative else [0]
    
    # Преобразование многочлена — кратные корни в простые
    def NMP_P_P(self, coeff_polynom: list) -> list:
        """Преобразование многочлена """
        # найдем производную многочлена
        derivate = self.DER_P_P(coeff_polynom)
        # найдем НОД многочлена и его производной
        gcd_polynom = self.GCD_PP_P(coeff_polynom, derivate)
        # находим частное от многочлена при делении на его НОД
        simple_polymon = self.DIV_PP_P(coeff_polynom, gcd_polynom)

        return simple_polymon



# Пример инициализации и вывода многочлена
if __name__ == '__main__':
    a = Polynomial('-2/3 3 4 -2')   #    -2/3  +  3X + 4X^2 - 2X^3
    print(a)

