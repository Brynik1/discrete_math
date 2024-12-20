from modules.Natural import *
from modules.Integer import *
from modules.Rational import *
from modules.Polynomial import *

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
def is_Polynomial(polynomial_str):
    coefficients = polynomial_str.split()
    return len(coefficients) > 0 and all(is_Rational(coefficient) for coefficient in coefficients)
def polynomial_to_coefficients(polynomial_str):
    if polynomial_str == '': return ''
    if is_Polynomial(polynomial_str): return polynomial_str
    polynomial_str = polynomial_str.replace('-','+-').replace(' ', '').replace('**','^')
    if polynomial_str[0] == '+': polynomial_str = polynomial_str[1:]
    coefficients = {}
    max_degree = 0
    for term in polynomial_str.split("+"):
        if 'x' in term:
            if "*" in term:
                coefficient, power = term.split("*")
                power = power.split("^")[1]
            elif '^' in term:
                coefficient, power = term.split("x^")
                if coefficient == '': coefficient = '1'
                elif coefficient == '-': coefficient = '-1'
            else:
                coefficient = term.split("x")[0]
                if coefficient == '': coefficient = '1'
                elif coefficient == '-': coefficient = '-1'
                power = '1'
        else:
            coefficient, power = term, '0'
        if not is_Natural(power): raise ValueError('Степени должны быть натуральными числами')
        if not is_Rational(coefficient): raise ValueError('Коэффициенты должны быть рациональными числами')
        if power in coefficients: raise ValueError('Дублирование степеней')

        # Добавление коэффициента в словарь
        power = int(power)
        coefficients[power] = coefficient
        max_degree = max(max_degree, power)

    # Формирование массива коэффициентов
    result = ['0'] * (max_degree + 1)
    for power, coefficient in coefficients.items():
        result[power] = coefficient
    return ' '.join(result)
def get_Natural(string):
    if not is_Natural(string): raise ValueError('Введенное число не является натуральным')
    return Natural(string)
def get_Integer(string):
    if not is_Integer(string): raise ValueError('Введенное число не является целым')
    return Integer(string)
def get_Rational(string):
    if not is_Rational(string): raise ValueError('Введенное число не является рациональным')
    return Rational(string)
def get_Polynomial(string):
    string = polynomial_to_coefficients(string)
    if not is_Polynomial(string): raise ValueError('Введенное число не является многочленом')
    return Polynomial(string)

if __name__ == '__main__':
    print(get_Natural(('123')))
    print(get_Integer(('-123')))
    print(get_Rational(('-123/35')))
    print(get_Polynomial('1x + 2 - x^2 - x^4'))
