from modules.Natural import Natural
from modules.Integer import Integer
from modules.Rational import Rational
from modules.Polynomial import Polynomial

if __name__ == '__main__':
    num1 = Natural('123')
    num2 = Integer('-542')
    num3 = Rational('43/67')
    polynom = Polynomial('2/3 -2 3 5 -3/2')

    print(num1)
    print(num2)
    print(num3)
    print(polynom)