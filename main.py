from modules.Natural import Natural, Natural_tests
from modules.Integer import Integer, Integer_initial_test
from modules.Rational import Rational, Rational_initial_test
from modules.Polynomial import Polynomial, Polynomial_initial_test

if __name__ == '__main__':
    # Пример инициализации и вывода
    num1 = Natural('123')
    num2 = Integer('-542')
    num3 = Rational('43/2')
    polynom = Polynomial('2/3 -2/1 3 5 -3/2')
    print(f'Натуральное:  {num1}')
    print(f'Целое:  {num2}')
    print(f'Рациональное:  {num3}')
    print(f'Многочлен:  {polynom}')
    print('\n\n')


    Natural_tests()  # Проверка натуральных
    print('\n')
    Integer_initial_test()  # Базовая проверка целых
    print('\n')
    Rational_initial_test()  # Базовая проверка рациональных
    print('\n')
    Polynomial_initial_test()   # Базовая проверка многочленов
    print('\n')