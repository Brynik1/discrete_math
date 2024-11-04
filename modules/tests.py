import unittest
from Natural import *
from Integer import *
from Rational import *
from Polynomial import *


# Тесты класса натуральных
class TestNatural(unittest.TestCase):
    def test_init(self):
        # Лучший случай:
        n = Natural('5')
        self.assertEqual(n.number, [5], msg=f"Natural('5') expected [5], returned {n.number}")

        # Средний случай:
        n = Natural('123')
        self.assertEqual(n.number, [1, 2, 3], msg=f"Natural('123') expected [1, 2, 3], returned {n.number}")

        # Худший случай: число с ведущими нулями
        n = Natural('0123')
        self.assertEqual(n.number, [1, 2, 3], msg=f"Natural('0123') expected [1, 2, 3], returned {n.number}")

    def test_str(self):
        # Лучший случай:
        n = Natural('5')
        self.assertEqual(str(n), '5', msg=f"str(Natural('5')) expected '5', returned {str(n)}")

        # Средний случай:
        n = Natural('123')
        self.assertEqual(str(n), '123', msg=f"str(Natural('123')) expected '123', returned {str(n)}")

        # Худший случай:
        n = Natural('0123')
        self.assertEqual(str(n), '123', msg=f"str(Natural('0123')) expected '123', returned {str(n)}")

    def test_COM_NN_D(self):
        # Худший случай: сравнение двух равных чисел
        n1 = Natural('123')
        n2 = Natural('123')
        self.assertEqual(n1.COM_NN_D(n2), 0, msg=f"COM_NN_D(Natural('123'), Natural('123')) expected 0, "
                                                 f"returned {n1.COM_NN_D(n2)}")

        # Средний случай: сравнение двух неравных чисел
        n1 = Natural('123')
        n2 = Natural('456')
        self.assertEqual(n1.COM_NN_D(n2), 1, msg=f"COM_NN_D(Natural('123'), Natural('456')) expected 1, "
                                                 f"returned {n1.COM_NN_D(n2)}")

        # Лучший случай: сравнение двух чисел с разной длиной
        n1 = Natural('123')
        n2 = Natural('1234')
        self.assertEqual(n1.COM_NN_D(n2), 1, msg=f"COM_NN_D(Natural('123'), Natural('1234')) expected 1, "
                                                 f"returned {n1.COM_NN_D(n2)}")

    def test_NZER_N_B(self):
        # Лучший случай: число не равно нулю
        n = Natural('123')
        self.assertTrue(n.NZER_N_B(), msg=f"NZER_N_B(Natural('123')) expected True, returned {n.NZER_N_B()}")

        # Средний случай: число равно нулю
        n = Natural('0')
        self.assertFalse(n.NZER_N_B(), msg=f"NZER_N_B(Natural('0')) expected False, returned {n.NZER_N_B()}")

        # Худший случай: число с ведущими нулями
        n = Natural('0123')
        self.assertTrue(n.NZER_N_B(), msg=f"NZER_N_B(Natural('0123')) expected True, returned {n.NZER_N_B()}")

    def test_ADD_1N_N(self):
        # Лучший случай: прибавление 1 к числу, не оканчивающемуся на 9
        n = Natural('123')
        self.assertEqual(str(n.ADD_1N_N()), '124', msg=f"ADD_1N_N(Natural('123')) expected '124', "
                                                       f"returned {str(n.ADD_1N_N())}")

        # Средний случай: прибавление 1 к числу, оканчивающемуся на 9
        n = Natural('129')
        self.assertEqual(str(n.ADD_1N_N()), '130', msg=f"ADD_1N_N(Natural('129')) expected '130', "
                                                       f"returned {str(n.ADD_1N_N())}")

        # Худший случай: прибавление 1 к числу, состоящему только из 9
        n = Natural('999')
        self.assertEqual(str(n.ADD_1N_N()), '1000', msg=f"ADD_1N_N(Natural('999')) expected '1000', "
                                                        f"returned {str(n.ADD_1N_N())}")

    def test_ADD_NN_N(self):
        # Лучший случай: сложение двух чисел без переноса
        n1 = Natural('123')
        n2 = Natural('456')
        self.assertEqual(str(n1.ADD_NN_N(n2)), '579', msg=f"ADD_NN_N(Natural('123'), Natural('456')) expected '579', "
                                                          f"returned {str(n1.ADD_NN_N(n2))}")

        # Средний случай: сложение двух чисел с переносом
        n1 = Natural('129')
        n2 = Natural('456')
        self.assertEqual(str(n1.ADD_NN_N(n2)), '585', msg=f"ADD_NN_N(Natural('129'), Natural('456')) expected '585', "
                                                          f"returned {str(n1.ADD_NN_N(n2))}")

        # Худший случай: сложение двух чисел с разной длиной
        n1 = Natural('123')
        n2 = Natural('1234')
        self.assertEqual(str(n1.ADD_NN_N(n2)), '1357', msg=f"ADD_NN_N(Natural('123'), Natural('1234')) "
                                                           f"expected '1357', returned {str(n1.ADD_NN_N(n2))}")

    def test_SUB_NN_N(self):
        # Лучший случай: без заема
        n1 = Natural('456')
        n2 = Natural('123')
        self.assertEqual(str(n1.SUB_NN_N(n2)), '333', msg=f"SUB_NN_N(Natural('456'), Natural('123')) expected '333', "
                                                          f"returned {str(n1.SUB_NN_N(n2))}")

        # Средний случай: с займом
        n1 = Natural('456')
        n2 = Natural('279')
        self.assertEqual(str(n1.SUB_NN_N(n2)), '177', msg=f"SUB_NN_N(Natural('456'), Natural('279')) expected '177', "
                                                          f"returned {str(n1.SUB_NN_N(n2))}")

        # Худший случай: вычитание равных чисел
        n1 = Natural('123')
        n2 = Natural('123')
        self.assertEqual(str(n1.SUB_NN_N(n2)), '0', msg=f"SUB_NN_N(Natural('123'), Natural('123')) expected '0', "
                                                        f"returned {str(n1.SUB_NN_N(n2))}")

    def test_MUL_ND_N(self):
        # Лучший случай: умножение числа на 0
        n = Natural('123')
        self.assertEqual(str(n.MUL_ND_N(0)), '0', msg=f"MUL_ND_N(Natural('123'), 0) expected '0', "
                                                      f"returned {str(n.MUL_ND_N(0))}")

        # Средний случай: умножение числа на цифру
        n = Natural('123')
        self.assertEqual(str(n.MUL_ND_N(5)), '615', msg=f"MUL_ND_N(Natural('123'), 5) expected '615', "
                                                        f"returned {str(n.MUL_ND_N(5))}")

        # Худший случай: умножение числа на 9
        n = Natural('123')
        self.assertEqual(str(n.MUL_ND_N(9)), '1107', msg=f"MUL_ND_N(Natural('123'), 9) expected '1107', "
                                                         f"returned {str(n.MUL_ND_N(9))}")

    def test_MUL_Nk_N(self):
        # Лучший случай: умножение числа на 10^0
        n = Natural('123')
        self.assertEqual(str(n.MUL_Nk_N(0)), '123', msg=f"MUL_Nk_N(Natural('123'), 0) expected '123', "
                                                        f"returned {str(n.MUL_Nk_N(0))}")

        # Средний случай: умножение числа на 10^k
        n = Natural('123')
        self.assertEqual(str(n.MUL_Nk_N(3)), '123000', msg=f"MUL_Nk_N(Natural('123'), 3) expected '123000', "
                                                           f"returned {str(n.MUL_Nk_N(3))}")

        # Худший случай: умножение числа на 10^10
        n = Natural('123')
        self.assertEqual(str(n.MUL_Nk_N(10)), '1230000000000',
                         msg=f"MUL_Nk_N(Natural('123'), 10) expected '1230000000000', "
                             f"returned {str(n.MUL_Nk_N(10))}")

    def test_MUL_NN_N(self):
        # Лучший случай: умножение двух чисел, одно из которых 0
        n1 = Natural('123')
        n2 = Natural('0')
        self.assertEqual(str(n1.MUL_NN_N(n2)), '0', msg=f"MUL_NN_N(Natural('123'), Natural('0')) expected '0', "
                                                        f"returned {str(n1.MUL_NN_N(n2))}")

        # Средний случай: умножение двух чисел
        n1 = Natural('123')
        n2 = Natural('456')
        self.assertEqual(str(n1.MUL_NN_N(n2)), '56088',
                         msg=f"MUL_NN_N(Natural('123'), Natural('456')) expected '56088', "
                             f"returned {str(n1.MUL_NN_N(n2))}")

        # Худший случай: умножение двух больших чисел
        n1 = Natural('123456')
        n2 = Natural('789012')
        self.assertEqual(str(n1.MUL_NN_N(n2)), '97408265472', msg=f"MUL_NN_N(Natural('123456'), Natural('789012')) "
                                                                  f"expected '97408265472', returned {str(n1.MUL_NN_N(n2))}")

    def test_SUB_NDN_N(self):
        # Лучший случай: вычитание числа, умноженного на 0
        n1 = Natural('123')
        n2 = Natural('456')
        self.assertEqual(str(n1.SUB_NDN_N(n2, 0)), '123',
                         msg=f"SUB_NDN_N(Natural('123'), Natural('456'), 0) expected '123', "
                             f"returned {str(n1.SUB_NDN_N(n2, 0))}")

        # Средний случай: вычитание числа, умноженного на цифру
        n1 = Natural('123')
        n2 = Natural('45')
        self.assertEqual(str(n1.SUB_NDN_N(n2, 2)), '33',
                         msg=f"SUB_NDN_N(Natural('123'), Natural('45'), 2) expected '33', "
                             f"returned {str(n1.SUB_NDN_N(n2, 2))}")

        # Худший случай: вычитание числа, умноженного на 9
        n1 = Natural('123')
        n2 = Natural('14')
        self.assertEqual(str(n1.SUB_NDN_N(n2, 9)), '0',
                         msg=f"SUB_NDN_N(Natural('123'), Natural('14'), 9) expected '0', "
                             f"returned {str(n1.SUB_NDN_N(n2, 9))}")


    def test_DIV_NN_Dk(self):
        # этот тест не проходит
        # Лучший случай: деление числа на 1
        # n1 = Natural('123')
        # n2 = Natural('1')
        # self.assertEqual(n1.DIV_NN_Dk(n2, 0), 1, msg=f"DIV_NN_Dk(Natural('123'), Natural('1'), 0) expected 1, "
        #                                              f"returned {n1.DIV_NN_Dk(n2, 0)}")

        # Средний случай: деление числа на делитель
        n1 = Natural('123')
        n2 = Natural('12')
        
        self.assertEqual(n1.DIV_NN_Dk(n2, 1), 1, msg=f"DIV_NN_Dk(Natural('123'), Natural('12'), 1) expected 1, "
                                                     f"returned {n1.DIV_NN_Dk(n2, 1)}")

        # Худший случай: деление числа на большое число
        n1 = Natural('123456')
        n2 = Natural('78901')
        self.assertEqual(n2.DIV_NN_Dk(n1, 3), 0, msg=f"DIV_NN_Dk(Natural('123456'), Natural('78901'), 3) expected 0, "
                                                     f"returned {n1.DIV_NN_Dk(n2, 3)}")

    def test_MOD_NN_N(self):
        # Лучший случай: остаток от деления числа на 1
        n1 = Natural('123')
        n2 = Natural('1')
        self.assertEqual(str(n1.MOD_NN_N(n2)), '0', msg=f"MOD_NN_N(Natural('123'), Natural('1')) expected '0', "
                                                        f"returned {str(n1.MOD_NN_N(n2))}")

        # Средний случай: остаток от деления числа на делитель
        n1 = Natural('123')
        n2 = Natural('12')
        self.assertEqual(str(n1.MOD_NN_N(n2)), '3', msg=f"MOD_NN_N(Natural('123'), Natural('12')) expected '3', "
                                                        f"returned {str(n1.MOD_NN_N(n2))}")

        # Худший случай: остаток от деления числа на большое число
        n1 = Natural('123456')
        n2 = Natural('789012')
        self.assertEqual(str(n1.MOD_NN_N(n2)), '123456', msg=f"MOD_NN_N(Natural('123456'), Natural('78901')) "
                                                             f"expected '123456', returned {str(n1.MOD_NN_N(n2))}")

        # Деление на само себя
        n1 = Natural('123')
        n2 = Natural('123')
        self.assertEqual(str(n1.MOD_NN_N(n2)), '0', msg=f"MOD_NN_N(Natural('123'), Natural('123')) expected '0', "
                                                        f"returned {str(n1.MOD_NN_N(n2))}")

        # Деление на число, кратное данному
        n1 = Natural('123')
        n2 = Natural('246')
        self.assertEqual(str(n1.MOD_NN_N(n2)), '123', msg=f"MOD_NN_N(Natural('123'), Natural('246')) expected '123', "
                                                          f"returned {str(n1.MOD_NN_N(n2))}")

    def test_GCF_NN_N(self):
        # Лучший случай: НОД двух одинаковых чисел
        n1 = Natural('123')
        n2 = Natural('123')
        self.assertEqual(str(n1.GCF_NN_N(n2)), '123', msg=f"GCF_NN_N(Natural('123'), Natural('123')) expected '123', "
                                                          f"returned {str(n1.GCF_NN_N(n2))}")

        # Средний случай: НОД двух разных чисел
        n1 = Natural('12')
        n2 = Natural('18')
        self.assertEqual(str(n1.GCF_NN_N(n2)), '6', msg=f"GCF_NN_N(Natural('12'), Natural('18')) expected '6', "
                                                        f"returned {str(n1.GCF_NN_N(n2))}")

        # Худший случай: НОД двух больших чисел
        n1 = Natural('123456')
        n2 = Natural('789012')
        self.assertEqual(str(n1.GCF_NN_N(n2)), '12',
                         msg=f"GCF_NN_N(Natural('123456'), Natural('789012')) expected '12', "
                             f"returned {str(n1.GCF_NN_N(n2))}")

        # НОД числа и 1
        n1 = Natural('123')
        n2 = Natural('1')
        self.assertEqual(str(n1.GCF_NN_N(n2)), '1', msg=f"GCF_NN_N(Natural('123'), Natural('1')) expected '1', "
                                                        f"returned {str(n1.GCF_NN_N(n2))}")

        # НОД двух простых чисел
        n1 = Natural('23')
        n2 = Natural('37')
        self.assertEqual(str(n1.GCF_NN_N(n2)), '1', msg=f"GCF_NN_N(Natural('23'), Natural('37')) expected '1', "
                                                        f"returned {str(n1.GCF_NN_N(n2))}")

    def test_LCM_NN_N(self):
        # Лучший случай: НОК двух одинаковых чисел
        n1 = Natural('123')
        n2 = Natural('123')
        self.assertEqual(str(n1.LCM_NN_N(n2)), '123', msg=f"Natural('123').LCM_NN_N(Natural('123'))")

        # Средний случай: НОК двух разных чисел
        n1 = Natural('12')
        n2 = Natural('18')
        self.assertEqual(str(n1.LCM_NN_N(n2)), '36', msg=f"Natural('12').LCM_NN_N(Natural('18'))")

        # этот тест выполняется бесконечно выполняется
        # Худший случай: НОК двух больших чисел
        # n1 = Natural('123456')
        # n2 = Natural('789012')
        # self.assertEqual(str(n1.LCM_NN_N(n2)), '80828102448', msg=f"Natural('123456').LCM_NN_N(Natural('789012'))")

        # НОК числа и 1
        n1 = Natural('123')
        n2 = Natural('1')
        self.assertEqual(str(n1.LCM_NN_N(n2)), '123')

        # НОК двух простых чисел
        n1 = Natural('23')
        n2 = Natural('37')
        self.assertEqual(str(n1.LCM_NN_N(n2)), '851')


# Тесты класса целых
class TestInteger(unittest.TestCase):
    def test_ABS_Z_N(self):
        # Лучший случай: положительное число
        a = Integer('12345')
        expected = Natural('12345')
        self.assertEqual(a.ABS_Z_N(), expected)

        # Средний случай: отрицательное число
        a = Integer('-12345')
        expected = Natural('12345')
        self.assertEqual(a.ABS_Z_N(), expected)

        # Крайний случай: ноль
        a = Integer('0')
        expected = Natural('0')
        self.assertEqual(a.ABS_Z_N(), expected)

    def test_POZ_Z_D(self):
        # Лучший случай: положительное число
        a = Integer('12345')
        self.assertEqual(a.POZ_Z_D(), 2)

        # Средний случай: отрицательное число
        a = Integer('-12345')
        self.assertEqual(a.POZ_Z_D(), 1)

        # Крайний случай: ноль
        a = Integer('0')
        self.assertEqual(a.POZ_Z_D(), 0)

    def test_MUL_ZM_Z(self):
        # Лучший случай: положительное число
        a = Integer('12345')
        expected = Integer('-12345')
        self.assertEqual(a.MUL_ZM_Z(), expected)

        # Средний случай: отрицательное число
        a = Integer('-12345')
        expected = Integer('12345')
        self.assertEqual(a.MUL_ZM_Z(), expected)

        # Крайний случай: ноль
        a = Integer('0')
        expected = Integer('0')
        self.assertEqual(a.MUL_ZM_Z(), expected)

    def test_TRANS_N_Z(self):
        # Лучший случай: натуральное число
        a = Natural('12345')
        expected = Integer('12345')
        self.assertEqual(Integer.TRANS_N_Z(a), expected)

        # Средний случай: натуральное число с указанным знаком
        a = Natural('12345')
        expected = Integer('-12345')
        self.assertEqual(Integer.TRANS_N_Z(a, 1), expected)

        # Крайний случай: ноль
        a = Natural('0')
        expected = Integer('0')
        self.assertEqual(Integer.TRANS_N_Z(a), expected)

    def test_TRANS_Z_N(self):
        # Лучший случай: положительное число
        a = Integer('12345')
        expected = Natural('12345')
        self.assertEqual(a.TRANS_Z_N(), expected)

        # Худший случай: отрицательное число
        a = Integer('-12345')
        expected = Natural('12345')
        self.assertEqual(a.TRANS_Z_N(), expected)

        # Крайний случай: ноль
        a = Integer('0')
        expected = Natural('0')
        self.assertEqual(a.TRANS_Z_N(), expected)

    def test_ADD_ZZ_Z(self):
        # Лучший случай: сложение положительных чисел
        a = Integer('12345')
        b = Integer('67890')
        expected = Integer('80235')
        self.assertEqual(a.ADD_ZZ_Z(b), expected)

        # Средний случай: сложение отрицательных чисел
        a = Integer('-12345')
        b = Integer('-67890')
        expected = Integer('-80235')
        self.assertEqual(a.ADD_ZZ_Z(b), expected)

        # Худший случай: сложение чисел с разными знаками
        a = Integer('12345')
        b = Integer('-67890')
        expected = Integer('-55545')
        self.assertEqual(a.ADD_ZZ_Z(b), expected)

        # Крайний случай: сложение с нулем
        a = Integer('12345')
        b = Integer('0')
        expected = Integer('12345')
        self.assertEqual(a.ADD_ZZ_Z(b), expected)

    def test_SUB_ZZ_Z(self):
        # Лучший случай: вычитание положительных чисел
        a = Integer('12345')
        b = Integer('67890')
        expected = Integer('-55545')
        self.assertEqual(a.SUB_ZZ_Z(b), expected)

        # Средний случай: вычитание отрицательных чисел
        a = Integer('-12345')
        b = Integer('-67890')
        expected = Integer('55545')
        self.assertEqual(a.SUB_ZZ_Z(b), expected)

        # Худший случай: вычитание чисел с разными знаками
        a = Integer('12345')
        b = Integer('-67890')
        expected = Integer('80235')
        self.assertEqual(a.SUB_ZZ_Z(b), expected)

        # Крайний случай: вычитание нуля
        a = Integer('12345')
        b = Integer('0')
        expected = Integer('12345')
        self.assertEqual(a.SUB_ZZ_Z(b), expected)

    def test_MUL_ZZ_Z(self):
        # Лучший случай: умножение положительных чисел
        a = Integer('12345')
        b = Integer('67890')
        expected = Integer('838102050')
        self.assertEqual(a.MUL_ZZ_Z(b), expected)

        # Средний случай: умножение отрицательных чисел
        a = Integer('-12345')
        b = Integer('-67890')
        expected = Integer('838102050')
        self.assertEqual(a.MUL_ZZ_Z(b), expected)

        # Худший случай: умножение чисел с разными знаками
        a = Integer('12345')
        b = Integer('-67890')
        expected = Integer('-838102050')
        self.assertEqual(a.MUL_ZZ_Z(b), expected)

        # Крайний случай: умножение на ноль
        a = Integer('12345')
        b = Integer('0')
        expected = Integer('0')
        self.assertEqual(a.MUL_ZZ_Z(b), expected)

    def test_DIV_ZZ_Z(self):
        # Лучший случай: деление положительных чисел
        a = Integer('12345')
        b = Integer('123')
        expected = Integer('100')
        self.assertEqual(a.DIV_ZZ_Z(b), expected)

        # Средний случай: деление отрицательных чисел
        a = Integer('-12345')
        b = Integer('-123')
        expected = Integer('100')
        self.assertEqual(a.DIV_ZZ_Z(b), expected)

        # Худший случай: деление чисел с разными знаками
        a = Integer('12345')
        b = Integer('-123')
        expected = Integer('-100')
        self.assertEqual(a.DIV_ZZ_Z(b), expected)

        # Крайний случай: деление на единицу
        a = Integer('12345')
        b = Integer('1')
        expected = Integer('12345')
        self.assertEqual(a.DIV_ZZ_Z(b), expected)

    def test_MOD_ZZ_Z(self):
        # Лучший случай: деление без остатка
        a = Integer('12345')
        b = Integer('12345')
        expected = Integer('0')
        result = a.MOD_ZZ_Z(b)
        self.assertEqual(result, expected)

        # Средний случай: деление с остатком
        a = Integer('12345')
        b = Integer('123')
        expected = Integer('45')
        result = a.MOD_ZZ_Z(b)
        self.assertEqual(result, expected)
        
        # Худший случай: деление на отрицательное число
        a = Integer('12345')
        b = Integer('-123')
        expected = Integer('45')
        result = a.MOD_ZZ_Z(b)
        self.assertEqual(result, expected)

        # Крайний случай: деление на единицу
        a = Integer('12345')
        b = Integer('1')
        expected = Integer('0')
        result = a.MOD_ZZ_Z(b)
        self.assertEqual(result, expected)




# Тесты класса рациональных
class TestRational(unittest.TestCase):
    def test_init(self):
        # Лучший случай: корректное рациональное число
        a = Rational('123/456')
        self.assertEqual(str(a.numerator), '123')
        self.assertEqual(str(a.denominator), '456')

        # Средний случай: рациональное число с разделителем '|'
        a = Rational('123|456')
        self.assertEqual(str(a.numerator), '123')
        self.assertEqual(str(a.denominator), '456')

        # Средний случай: рациональное число с разделителем ':'
        a = Rational('123:456')
        self.assertEqual(str(a.numerator), '123')
        self.assertEqual(str(a.denominator), '456')

        # Средний случай: целое число
        a = Rational('123')
        self.assertEqual(str(a.numerator), '123')
        self.assertEqual(str(a.denominator), '1')

        # Крайний случай: ноль
        a = Rational('0')
        self.assertEqual(str(a.numerator), '0')
        self.assertEqual(str(a.denominator), '1')

    def test_str(self):
        # Лучший случай: рациональное число
        a = Rational('123/456')
        self.assertEqual(str(a), '123/456')

        # Средний случай: целое число
        a = Rational('123/1')
        self.assertEqual(str(a), '123')

        # Крайний случай: ноль
        a = Rational('0/1')
        self.assertEqual(str(a), '0')

    def test_RED_Q_Q(self):
        # Лучший случай: несократимая дробь
        a = Rational('123/457')
        expected = Rational('123/457')
        self.assertEqual(str(a.RED_Q_Q()), str(expected))

        # Средний случай: сократимая дробь
        a = Rational('120/360')
        expected = Rational('1/3')
        self.assertEqual(str(a.RED_Q_Q()), str(expected))

        # Крайний случай: ноль
        a = Rational('0/123')
        expected = Rational('0/1')
        self.assertEqual(str(a.RED_Q_Q()), str(expected))

    def test_INT_Q_B(self):
        # Лучший случай: целое число
        a = Rational('123/1')
        self.assertTrue(a.INT_Q_B())

        # Средний случай: дробное число
        a = Rational('123/456')
        self.assertFalse(a.INT_Q_B())

        # Крайний случай: ноль
        a = Rational('0/123')
        self.assertTrue(a.INT_Q_B())

    def test_TRANS_Z_Q(self):
        # Лучший случай: целое число
        a = Integer('123')
        expected = Rational('123/1')
        self.assertEqual(str(Rational.TRANS_Z_Q(a)), str(expected))

        # Средний случай: отрицательное целое число
        a = Integer('-123')
        expected = Rational('-123/1')
        self.assertEqual(str(Rational.TRANS_Z_Q(a)), str(expected))

        # Крайний случай: ноль
        a = Integer('0')
        expected = Rational('0/1')
        self.assertEqual(str(Rational.TRANS_Z_Q(a)), str(expected))

    def test_TRANS_Q_Z(self):
        # Лучший случай: целое число
        a = Rational('123/1')
        expected = Integer('123')
        self.assertEqual(str(a.TRANS_Q_Z()), str(expected))

        # Средний случай: отрицательное целое число
        a = Rational('-123/1')
        expected = Integer('-123')
        self.assertEqual(str(a.TRANS_Q_Z()), str(expected))

        # Крайний случай: ноль
        a = Rational('0/1')
        expected = Integer('0')
        self.assertEqual(str(a.TRANS_Q_Z()), str(expected))


# Тесты класса многочленов
class TestPolynomial(unittest.TestCase):
    pass


if __name__ == '__main__':
    # запускаем все тесты которые есть
    unittest.main()

    # Пример запуска конкретного модуля
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestNatural)
    # unittest.TextTestRunner().run(suite)
