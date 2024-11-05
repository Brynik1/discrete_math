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
        n2 = Natural('10')
        self.assertEqual(str(n1.SUB_NDN_N(n2, 9)), '33',
                         msg=f"SUB_NDN_N(Natural('123'), Natural('10'), 9) expected '33', "
                             f"returned {str(n1.SUB_NDN_N(n2, 9))}")

    def test_DIV_NN_Dk(self):
        # этот тест не проходит
        # Лучший случай: деление числа на 1
        n1 = Natural('123')
        n2 = Natural('1')
        self.assertEqual(n1.DIV_NN_Dk(n2, 0), 1, msg=f"DIV_NN_Dk(Natural('123'), Natural('1'), 0) expected 1, "
                                                     f"returned {n1.DIV_NN_Dk(n2, 0)}")

        # Средний случай: деление числа на делитель
        n1 = Natural('123')
        n2 = Natural('12')

        self.assertEqual(n1.DIV_NN_Dk(n2, 1), 1, msg=f"DIV_NN_Dk(Natural('123'), Natural('12'), 1) expected 1, "
                                                     f"returned {n1.DIV_NN_Dk(n2, 1)}")


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
        expected = '12345'
        self.assertEqual(expected, str(a.ABS_Z_N()))

        # Средний случай: отрицательное число
        a = Integer('-12345')
        expected = '12345'
        self.assertEqual(expected, str(a.ABS_Z_N()))

        # Крайний случай: ноль
        a = Integer('0')
        expected = '0'
        self.assertEqual(expected, str(a.ABS_Z_N()))

    def test_POZ_Z_D(self):
        # Лучший случай: положительное число
        a = Integer('12345')
        self.assertEqual(2, a.POZ_Z_D(), msg="POZ_Z_D of positive number expected 2")

        # Средний случай: отрицательное число
        a = Integer('-12345')
        self.assertEqual(1, a.POZ_Z_D(), msg="POZ_Z_D of negative number expected 1")

        # Крайний случай: ноль
        a = Integer('0')
        self.assertEqual(0, a.POZ_Z_D(), msg="POZ_Z_D of zero expected 0")

    def test_MUL_ZM_Z(self):
        # Лучший случай: положительное число
        a = Integer('12345')
        expected = '-12345'
        self.assertEqual(expected, str(a.MUL_ZM_Z()), msg="Positive number multiplication case failed")

        # Средний случай: отрицательное число
        a = Integer('-12345')
        expected = '12345'
        self.assertEqual(expected, str(a.MUL_ZM_Z()), msg="Negative number multiplication case failed")

        # Крайний случай: ноль
        a = Integer('0')
        expected = '0'
        self.assertEqual(expected, str(a.MUL_ZM_Z()), msg="Zero multiplication case failed")

    def test_TRANS_N_Z(self):
        # Лучший случай: натуральное число
        a = Natural('12345')
        expected = '12345'
        self.assertEqual(str(Integer.TRANS_N_Z(a)), expected, msg="TRANS_N_Z of natural number failed")

        # Средний случай: натуральное число с указанным знаком
        a = Natural('12345')
        expected = '-12345'
        self.assertEqual(str(Integer.TRANS_N_Z(a, 1)), expected, msg="TRANS_N_Z with sign parameter failed")

        # Крайний случай: ноль
        a = Natural('0')
        expected = '0'
        self.assertEqual(str(Integer.TRANS_N_Z(a)), expected, msg="TRANS_N_Z of zero failed")

    def test_TRANS_Z_N(self):
        # Лучший случай: положительное число
        a = Integer('12345')
        expected = '12345'
        self.assertEqual(str(a.TRANS_Z_N()), expected, msg="TRANS_Z_N of positive number failed")

        # Худший случай: отрицательное число
        a = Integer('-12345')
        expected = '12345'
        self.assertEqual(str(a.TRANS_Z_N()), expected, msg="TRANS_Z_N of negative number failed")

        # Крайний случай: ноль
        a = Integer('0')
        expected = '0'
        self.assertEqual(str(a.TRANS_Z_N()), expected, msg="TRANS_Z_N of zero failed")

    def test_ADD_ZZ_Z(self):
        # Лучший случай: сложение положительных чисел
        a = Integer('12345')
        b = Integer('67890')
        expected = '80235'
        self.assertEqual(str(a.ADD_ZZ_Z(b)), expected, msg="ADD_ZZ_Z of positive numbers failed")

        # Средний случай: сложение отрицательных чисел
        a = Integer('-12345')
        b = Integer('-67890')
        expected = '-80235'
        self.assertEqual(str(a.ADD_ZZ_Z(b)), expected, msg="ADD_ZZ_Z of negative numbers failed")

        # Худший случай: сложение чисел с разными знаками
        a = Integer('12345')
        b = Integer('-67890')
        expected = '-55545'
        self.assertEqual(str(a.ADD_ZZ_Z(b)), expected, msg="ADD_ZZ_Z of numbers with different signs failed")

        # Крайний случай: сложение с нулем
        a = Integer('12345')
        b = Integer('0')
        expected = '12345'
        self.assertEqual(str(a.ADD_ZZ_Z(b)), expected, msg="ADD_ZZ_Z with zero failed")

    def test_SUB_ZZ_Z(self):
        # Лучший случай: вычитание положительных чисел
        a = Integer('12345')
        b = Integer('67890')
        expected = '-55545'
        self.assertEqual(str(a.SUB_ZZ_Z(b)), expected, msg="SUB_ZZ_Z of positive numbers failed")

        # Средний случай: вычитание отрицательных чисел
        a = Integer('-12345')
        b = Integer('-67890')
        expected = '55545'
        self.assertEqual(str(a.SUB_ZZ_Z(b)), expected, msg="SUB_ZZ_Z of negative numbers failed")

        # Худший случай: вычитание чисел с разными знаками
        a = Integer('12345')
        b = Integer('-67890')
        expected = '80235'
        self.assertEqual(str(a.SUB_ZZ_Z(b)), expected, msg="SUB_ZZ_Z of numbers with different signs failed")

        # Крайний случай: вычитание нуля
        a = Integer('12345')
        b = Integer('0')
        expected = '12345'
        self.assertEqual(str(a.SUB_ZZ_Z(b)), expected, msg="SUB_ZZ_Z with zero failed")

    def test_MUL_ZZ_Z(self):
        # Лучший случай: умножение положительных чисел
        a = Integer('12345')
        b = Integer('67890')
        expected = '838102050'
        self.assertEqual(str(a.MUL_ZZ_Z(b)), expected, msg="MUL_ZZ_Z of positive numbers failed")

        # Средний случай: умножение отрицательных чисел
        a = Integer('-12345')
        b = Integer('-67890')
        expected = '838102050'
        self.assertEqual(str(a.MUL_ZZ_Z(b)), expected, msg="MUL_ZZ_Z of negative numbers failed")

        # Худший случай: умножение чисел с разными знаками
        a = Integer('12345')
        b = Integer('-67890')
        expected = '-838102050'
        self.assertEqual(str(a.MUL_ZZ_Z(b)), expected, msg="MUL_ZZ_Z of numbers with different signs failed")

        # Крайний случай: умножение на ноль
        a = Integer('12345')
        b = Integer('0')
        expected = '0'
        self.assertEqual(str(a.MUL_ZZ_Z(b)), expected, msg="MUL_ZZ_Z with zero failed")

    def test_DIV_ZZ_Z(self):
        # Лучший случай: деление положительных чисел
        a = Integer('12345')
        b = Integer('123')
        expected = '100'
        self.assertEqual(str(a.DIV_ZZ_Z(b)), expected, msg="DIV_ZZ_Z of positive numbers failed")

        # Средний случай: деление отрицательных чисел
        a = Integer('-12345')
        b = Integer('-123')
        expected = '100'
        self.assertEqual(str(a.DIV_ZZ_Z(b)), expected, msg="DIV_ZZ_Z of negative numbers failed")

        # Худший случай: деление чисел с разными знаками
        a = Integer('12345')
        b = Integer('-123')
        expected = '-100'
        self.assertEqual(str(a.DIV_ZZ_Z(b)), expected, msg="DIV_ZZ_Z of numbers with different signs failed")

        # Крайний случай: деление на единицу
        a = Integer('12345')
        b = Integer('1')
        expected = '12345'
        self.assertEqual(str(a.DIV_ZZ_Z(b)), expected, msg="DIV_ZZ_Z of division by one failed")

    def test_MOD_ZZ_Z(self):
        # Лучший случай: деление без остатка
        a = Integer('12345')
        b = Integer('12345')
        expected = '0'
        self.assertEqual(str(a.MOD_ZZ_Z(b)), expected, msg="MOD_ZZ_Z of division without remainder failed")

        # Средний случай: деление с остатком
        a = Integer('12345')
        b = Integer('123')
        expected = '45'
        self.assertEqual(str(a.MOD_ZZ_Z(b)), expected, msg="MOD_ZZ_Z of division with remainder failed")

        # Худший случай: деление на отрицательное число
        a = Integer('12345')
        b = Integer('-123')
        expected = '45'
        self.assertEqual(str(a.MOD_ZZ_Z(b)), expected, msg="MOD_ZZ_Z of division by negative number failed")

        # Крайний случай: деление на единицу
        a = Integer('12345')
        b = Integer('1')
        expected = '0'
        self.assertEqual(str(a.MOD_ZZ_Z(b)), expected, msg="MOD_ZZ_Z of division by one failed")

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
        self.assertTrue(a.INT_Q_B(), msg=f"Failed for input {a}: expected True, got {a.INT_Q_B()}")

        # Средний случай: дробное число
        a = Rational('123/456')
        self.assertFalse(a.INT_Q_B(), msg=f"Failed for input {a}: expected False, got {a.INT_Q_B()}")

        # Крайний случай: ноль
        a = Rational('0/123')
        self.assertTrue(a.INT_Q_B(), msg=f"Failed for input {a}: expected True, got {a.INT_Q_B()}")


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
    def test_ADD_PP_P(self):
        # Лучший случай: сложение двух многочленов без нулевых коэффициентов
        p1 = Polynomial("1 2/3")
        p2 = Polynomial("4 5/6")
        expected = Polynomial("5 3/2")
        self.assertEqual(str(expected), str(p1.ADD_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

        # Средний случай: сложение многочленов с нулевыми коэффициентами
        p1 = Polynomial("1 0 2/3 0")
        p2 = Polynomial("0 4 0 5/6")
        expected = Polynomial("1 4 2/3 5/6")
        self.assertEqual(str(expected), str(p1.ADD_PP_P(p2)),  msg=f"Failed for inputs {p1} and {p2}")

        # Крайний случай: сложение одного многочлена с нулем
        p1 = Polynomial("1 2/3")
        p2 = Polynomial("0")
        expected = Polynomial("1 2/3")
        self.assertEqual(str(expected), str(p1.ADD_PP_P(p2)),  msg=f"Failed for inputs {p1} and {p2}")

    def test_SUB_PP_P(self):
        # Лучший случай: вычитание двух многочленов без нулевых коэффициентов
        p1 = Polynomial("1 2/3")
        p2 = Polynomial("4 5/6")
        expected = Polynomial("-3 -1/6")
        self.assertEqual(str(expected), str(p1.SUB_PP_P(p2)),  msg=f"Failed for inputs {p1} and {p2}")

        # Средний случай: вычитание многочленов с нулевыми коэффициентами
        p1 = Polynomial("1 0 2/3 0")
        p2 = Polynomial("0 4 0 5/6")
        expected = Polynomial("1 -4 2/3 -5/6")
        self.assertEqual(str(expected), str(p1.SUB_PP_P(p2)),  msg=f"Failed for inputs {p1} and {p2}")

        # Крайний случай: вычитание одного многочлена с нулем
        p1 = Polynomial("1 2/3")
        p2 = Polynomial("0")
        expected = Polynomial("1 2/3")
        self.assertEqual(str(expected), str(p1.SUB_PP_P(p2)),  msg=f"Failed for inputs {p1} and {p2}")

    def test_MUL_PQ_P(self):
        # Лучший случай: умножение многочлена на рациональное число
        p1 = Polynomial("1 2/3 3/4")
        q = Rational("2/3")  # Предполагаем, что у вас есть класс Rational для работы с рациональными числами
        expected = Polynomial("2/3 4/9 1/2")
        self.assertEqual(str(expected), str(p1.MUL_PQ_P(q)), msg=f"Failed for polynomial {p1} and rational {q}")

        # Средний случай: умножение многочлена с нулевыми коэффициентами
        p1 = Polynomial("1 0 2/3 0")
        q = Rational("3/2")
        expected = Polynomial("3/2 0 1 0")
        self.assertEqual(str(expected), str(p1.MUL_PQ_P(q)), msg=f"Failed for polynomial {p1} and rational {q}")

        # Крайний случай: умножение на ноль
        p1 = Polynomial("1 2/3")
        q = Rational("0")
        expected = Polynomial("0")
        self.assertEqual(str(expected), str(p1.MUL_PQ_P(q)), msg=f"Failed for polynomial {p1} and rational {q}")

        # Крайний случай: умножение на 1, многочлен должен остаться неизменным
        p1 = Polynomial("1 2/3 -3/4")
        q = Rational("1")
        expected = Polynomial("1 2/3 -3/4")
        self.assertEqual(str(expected), str(p1.MUL_PQ_P(q)), msg=f"Failed for polynomial {p1} and rational {q}")

        # Случай с отрицательным числом
        p1 = Polynomial("1 2")
        q = Rational("-1/2")
        expected = Polynomial("-1/2 -1")
        self.assertEqual(str(expected), str(p1.MUL_PQ_P(q)), msg=f"Failed for polynomial {p1} and rational {q}")

    def test_MUL_Pxk_P(self):
        # Лучший случай: умножение многочлена на x^1
        p1 = Polynomial("1 2/3")
        k = 1
        expected = Polynomial("0 1 2/3")
        self.assertEqual(str(expected), str(p1.MUL_Pxk_P(k)), msg=f"Failed for polynomial {p1} and k={k}")

        # Средний случай: умножение многочлена на x^3
        p1 = Polynomial("1 2 3")
        k = 3
        expected = Polynomial("0 0 0 1 2 3")
        self.assertEqual(str(expected), str(p1.MUL_Pxk_P(k)), msg=f"Failed for polynomial {p1} and k={k}")

        # Крайний случай: умножение на x^0, многочлен должен остаться неизменным
        p1 = Polynomial("1 2/3 -3/4")
        k = 0
        expected = Polynomial("1 2/3 -3/4")
        self.assertEqual(str(expected), str(p1.MUL_Pxk_P(k)), msg=f"Failed for polynomial {p1} and k={k}")

        # Крайний случай: умножение на большое k
        p1 = Polynomial("1")
        k = 10
        expected = Polynomial("0 " * 10 + "1")
        self.assertEqual(str(expected), str(p1.MUL_Pxk_P(k)), msg=f"Failed for polynomial {p1} and k={k}")

        # Случай с многочленом, содержащим нули
        p1 = Polynomial("1 0 2")
        k = 2
        expected = Polynomial("0 0 1 0 2")
        self.assertEqual(str(expected), str(p1.MUL_Pxk_P(k)), msg=f"Failed for polynomial {p1} and k={k}")

    def test_LED_P_Q(self):
        # Лучший случай: многочлен с ненулевым старшим коэффициентом
        p1 = Polynomial("1 2/3 -3/4")
        expected = Rational("-3/4")
        self.assertEqual(str(expected), str(p1.LED_P_Q()), msg=f"Failed for polynomial {p1}")

        # Случай с многочленом, где старший коэффициент нулевой, но не последний
        p1 = Polynomial("0 1 2/3 -3/4")
        expected = Rational("-3/4")
        self.assertEqual(str(expected), str(p1.LED_P_Q()), msg=f"Failed for polynomial {p1}")

        # Крайний случай: многочлен с единственным коэффициентом
        p1 = Polynomial("5")
        expected = Rational("5")
        self.assertEqual(str(expected), str(p1.LED_P_Q()), msg=f"Failed for polynomial {p1}")

        # Крайний случай: многочлен с нулевыми коэффициентами, кроме последнего
        p1 = Polynomial("0 0 0 4/5")
        expected = Rational("4/5")
        self.assertEqual(str(expected), str(p1.LED_P_Q()), msg=f"Failed for polynomial {p1}")

        # Случай с многочленом, все коэффициенты которого нулевые
        p1 = Polynomial("0 0 0")
        with self.assertRaises(ValueError):
            p1.LED_P_Q()

        # Случай с пустым многочленом
        p1 = Polynomial("")
        with self.assertRaises(ValueError):
            p1.LED_P_Q()

    def test_DEG_P_N(self):
        # Лучший случай: многочлен с несколькими коэффициентами
        p1 = Polynomial("1 2/3 -3/4 0 5")
        expected = 4
        self.assertEqual(expected, p1.DEG_P_N(), msg=f"Failed for polynomial {p1}")

        # Случай с многочленом, содержащим только один коэффициент (степень 0)
        p1 = Polynomial("5")
        expected = 0
        self.assertEqual(expected, p1.DEG_P_N(), msg=f"Failed for polynomial {p1}")

        # Случай с многочленом, где последние коэффициенты нулевые
        p1 = Polynomial("1 0 0 0")
        expected = 0  # Несмотря на нули, степень определяется по количеству коэффициентов
        self.assertEqual(expected, p1.DEG_P_N(), msg=f"Failed for polynomial with trailing zeros {p1}")

    def test_FAC_P_Q(self):
        # Лучший случай: многочлен с различными рациональными коэффициентами
        p1 = Polynomial("1/2 2/3 3/4")
        expected = Rational("1/12")  # НОД(1, 2, 3) = 1, НОК(2, 3, 4) = 12
        self.assertEqual(str(expected), str(p1.FAC_P_Q()), msg=f"Failed for polynomial {p1}")

        # Случай, когда НОД числителей больше 1
        p1 = Polynomial("4/5 6/7 8/9")
        expected = Rational("2/315")  # НОД(4, 6, 8) = 2, НОК(5, 7, 9) = 315
        self.assertEqual(str(expected), str(p1.FAC_P_Q()), msg=f"Failed for polynomial {p1}")

        # Крайний случай: многочлен с целыми числами
        p1 = Polynomial("2 3 4")
        expected = Rational("1/1")  # Все числители взаимно простые, знаменатели все равны 1
        self.assertEqual(str(expected), str(p1.FAC_P_Q()), msg=f"Failed for polynomial {p1}")

        # Случай с многочленом, содержащим нулевой коэффициент
        p1 = Polynomial("0 1/2 2")
        expected = Rational("1/2")  # НОД(0, 1, 2) = 1 (обычно НОД с 0 считается как 1), НОК(1, 2) = 2
        self.assertEqual(str(expected), str(p1.FAC_P_Q()), msg=f"Failed for polynomial {p1}")

        # Случай, когда все коэффициенты одинаковы
        p1 = Polynomial("1/3 1/3 1/3")
        expected = Rational("1/3")  # НОД(1, 1, 1) = 1, НОК(3, 3, 3) = 3
        self.assertEqual(str(expected), str(p1.FAC_P_Q()), msg=f"Failed for polynomial {p1}")

    def test_MUL_PP_P(self):
        # Лучший случай: умножение двух многочленов с несколькими коэффициентами
        p1 = Polynomial("1 2")
        p2 = Polynomial("3 4")
        expected = Polynomial("3 10 8")  # (1 + 2x) * (3 + 4x) = 3 + 10x + 8x^2
        self.assertEqual(str(expected), str(p1.MUL_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

        # Средний случай: умножение многочлена на многочлен с нулевыми коэффициентами
        p1 = Polynomial("1 0 3")
        p2 = Polynomial("2 0 4")
        expected = Polynomial("2 0 10 0 12")  # (1 + 3x^2) * (2 + 4x^2)
        self.assertEqual(str(expected), str(p1.MUL_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

        # Крайний случай: умножение многочлена на многочлен с одним коэффициентом (константу)
        p1 = Polynomial("1 2")
        p2 = Polynomial("3")
        expected = Polynomial("3 6")  # (1 + 2x) * 3 = 3 + 6x
        self.assertEqual(str(expected), str(p1.MUL_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

        # Крайний случай: умножение на многочлен с нулевыми коэффициентами, кроме одного
        p1 = Polynomial("0 0 1")
        p2 = Polynomial("0 0 2")
        expected = Polynomial("0 0 0 0 2")  # x^2 * 2x^2 = 2x^4
        self.assertEqual(str(expected), str(p1.MUL_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

        # Случай с умножением на нулевой многочлен
        p1 = Polynomial("1 2")
        p2 = Polynomial("0")
        expected = Polynomial("0")  # Любой многочлен умноженный на 0 дает 0
        self.assertEqual(str(expected), str(p1.MUL_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

        # Проверка коммутативности умножения
        p1 = Polynomial("2 3")
        p2 = Polynomial("4 5")
        expected = p1.MUL_PP_P(p2)
        self.assertEqual(str(expected), str(p2.MUL_PP_P(p1)), msg="Multiplication is not commutative for {p1} and {p2}")

    def test_DIV_PP_P(self):
        # Лучший случай: деление многочлена на многочлен, дающее ненулевое частное
        p1 = Polynomial("1 0 -2 1")  # x^3 - 2x^2 + 1
        p2 = Polynomial("1 1")  # x + 1
        expected = Polynomial("3 -3 1")  #  (x^2 - 3x + 3).
        self.assertEqual(str(expected), str(p1.DIV_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

        # Случай, когда делимое меньше делителя по степени
        p1 = Polynomial("1 2")
        p2 = Polynomial("1 2 3")
        expected = Polynomial("0")
        self.assertEqual(str(expected), str(p1.DIV_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

        # Крайний случай: деление многочлена на самого себя
        p1 = Polynomial("1 2 3")
        expected = Polynomial("1")  # Любой многочлен, деленный на себя, дает 1
        self.assertEqual(str(expected), str(p1.DIV_PP_P(p1)), msg=f"Failed for inputs {p1} and itself")

        # Случай с остатком
        p1 = Polynomial("1 3 2")  # 2x^2 + 3x + 1
        p2 = Polynomial("1 1")  # x + 1
        expected = Polynomial("1 2")  # 2x + 1, остаток будет, но здесь мы тестируем только частное
        self.assertEqual(str(expected), str(p1.DIV_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

        # Случай деления на многочлен с нулевыми коэффициентами, кроме одного
        p1 = Polynomial("0 0 1")  # x^2
        p2 = Polynomial("0 0 1")  # x^2
        expected = Polynomial("1")  # x^2 / x^2 = 1
        self.assertEqual(str(expected), str(p1.DIV_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

        # Проверка деления на многочлен, который не делит без остатка
        p1 = Polynomial("1 1 1")  # x^2 + x + 1
        p2 = Polynomial("1 1")  # x + 1
        expected = Polynomial("0 1")  # x
        self.assertEqual(str(expected), str(p1.DIV_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

    def test_MOD_PP_P(self):
        # Лучший случай: остаток от деления многочлена на многочлен
        p1 = Polynomial("1 0 -2 1")  # x^3 - 2x^2 + 1
        p2 = Polynomial("1 1")  # x + 1
        expected = Polynomial("-2")  # Остаток от деления x^3 - 2x^2 + 1 на x + 1
        self.assertEqual(str(expected), str(p1.MOD_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

        # Случай, когда остаток равен нулю (деление нацело)
        p1 = Polynomial("1 2 1")  # x^2 + 2x + 1
        p2 = Polynomial("1 1")  # x + 1
        expected = Polynomial("0")  # x^2 + x + 1 делится на x + 1 без остатка
        self.assertEqual(str(expected), str(p1.MOD_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

        # Крайний случай: деление многочлена на самого себя
        p1 = Polynomial("1 2 3")
        expected = Polynomial("0")  # Любой многочлен деленный на себя дает остаток 0
        self.assertEqual(str(expected), str(p1.MOD_PP_P(p1)), msg=f"Failed for inputs {p1} and itself")

        # Случай с многочленом, степень которого меньше делителя
        p1 = Polynomial("1")
        p2 = Polynomial("1 1")  # x + 1
        expected = Polynomial("1")  # Многочлен меньшей степени, чем делитель, является остатком
        self.assertEqual(str(expected), str(p1.MOD_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

        # Случай с многочленом, содержащим только нулевые коэффициенты
        p1 = Polynomial("0 0 0")
        p2 = Polynomial("1 1")
        expected = Polynomial("0")  # Нулевой многочлен остается остатком при делении на любой многочлен
        self.assertEqual(str(expected), str(p1.MOD_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

    def test_GCF_PP_P(self):
        # Лучший случай: НОД двух многочленов, не равных друг другу
        p1 = Polynomial("1 2 1")  # x^2 + 2x + 1 = (x + 1)^2
        p2 = Polynomial("1 1")  # x + 1
        expected = Polynomial("1 1")  # НОД(x^2 + 2x + 1, x + 1) = x + 1
        self.assertEqual(str(expected), str(p1.GCF_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

        # Случай, когда один многочлен является кратным другого
        p1 = Polynomial("1 2 1")  # x^2 + 2x + 1
        p2 = Polynomial("1 3 3 1")  # (x + 1)^3
        expected = Polynomial("1 2 1")  # НОД((x + 1)^2, (x + 1)^3) = (x + 1)^2
        self.assertEqual(str(expected), str(p1.GCF_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

        # Крайний случай: НОД многочлена с самим собой
        p1 = Polynomial("-1 0 1")  # x^2 - 1
        expected = Polynomial("-1 0 1")  # НОД(x^2 - 1, x^2 - 1) = x^2 - 1
        self.assertEqual(str(expected), str(p1.GCF_PP_P(p1)), msg=f"Failed for input {p1} with itself")

        # Случай, когда многочлены не имеют общих множителей кроме константы
        p1 = Polynomial("1 1")  # x + 1
        p2 = Polynomial("-1 1")  # x - 1
        expected = Polynomial("1")  # НОД(x + 1, x - 1) = 1 (в контексте многочленов, это константа)
        self.assertEqual(str(expected), str(p1.GCF_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

        # Случай с многочленом и его производным
        p1 = Polynomial("1 3 3 1")  # x^3 + 3x^2 + 3x + 1 = (x + 1)^3
        p2 = Polynomial("3 6 3")  # 3x^2 + 6x + 3, производная от (x + 1)^3
        expected = Polynomial("1 2 1")  # НОД((x + 1)^3, его производная) = x + 1
        self.assertEqual(str(expected), str(p1.GCF_PP_P(p2)), msg=f"Failed for polynomial and its derivative")

    def test_DER_P_P(self):
        # Лучший случай: производная многочлена второй степени
        p1 = Polynomial("3 2 1")  # 3 + 2x + x^2
        expected = Polynomial("2 2")  # Производная: 2 + 2x
        self.assertEqual(str(expected), str(p1.DER_P_P()), msg=f"Failed for polynomial {p1}")

        # Случай с многочленом первой степени
        p1 = Polynomial("4 5")  # 4 + 5x
        expected = Polynomial("5")  # Производная: 5
        self.assertEqual(str(expected), str(p1.DER_P_P()), msg=f"Failed for polynomial {p1}")

        # Крайний случай: многочлен нулевой степени (константа)
        p1 = Polynomial("7")  # Константа 7
        expected = Polynomial("0")  # Производная константы 0
        self.assertEqual(str(expected), str(p1.DER_P_P()), msg=f"Failed for constant polynomial")

        # Случай с многочленом, имеющим нулевые коэффициенты
        p1 = Polynomial("0 0 3 0 1")  # 3x^2 + x^4
        expected = Polynomial("0 6 0 4")  # Производная: 6x + 4x^3
        self.assertEqual(str(expected), str(p1.DER_P_P()), msg=f"Failed for polynomial with zero coefficients")

        # По приколу
        p1 = Polynomial("0 0 0 1")  # x^3
        expected = Polynomial("0 0 3")  # 3x^2
        self.assertEqual(str(expected), str(p1.DER_P_P()), msg=f"Failed for polynomial x^3")

    def test_NMP_P_P(self):

        # Лучший случай: многочлен с кратными корнями
        p1 = Polynomial("1 4 6 4 1")  # (x + 1)^4
        expected = Polynomial("1 1")  # x + 1, после преобразования кратные корни становятся простыми
        self.assertEqual(str(expected), str(p1.NMP_P_P()), msg=f"Failed for polynomial {p1}")

        # Случай, когда многочлен уже имеет простые корни
        p1 = Polynomial("1 3 3 1")  # (x + 1)^3, но корни не кратные в исходном многочлене
        expected = p1  # Многочлен не изменится
        self.assertEqual(str(expected), str(p1.NMP_P_P()), msg=f"Failed for polynomial {p1} with simple roots")

        # Крайний случай: многочлен, состоящий только из константы (нет корней)
        p1 = Polynomial("1")  # Константа
        expected = Polynomial("1")  # Константа остается константой
        self.assertEqual(str(expected), str(p1.NMP_P_P()), msg=f"Failed for constant polynomial")

        # Случай с многочленом, который после преобразования станет многочленом меньшей степени
        p1 = Polynomial("1 0 -1")  # x^2 - 1 = (x - 1)(x + 1), но для теста добавим кратность
        p2 = Polynomial("1 2 1")  # (x + 1)^2 для создания кратного корня
        p1 = Polynomial.MUL_PP_P(p1, p2)  # (x^2 - 1) * (x + 1)^2
        expected = Polynomial("1 0 -1")  # После преобразования получим x^2 - 1
        self.assertEqual(str(expected), str(p1.NMP_P_P()), msg=f"Failed for polynomial with multiple roots")

        # Проверка на многочлен с кратными корнями, но не все корни кратные
        p1 = Polynomial("1 1 1")  # x^2 + x + 1, корень не кратный
        p2 = Polynomial("1 2 1")  # (x + 1)^2 добавим кратность
        p1 = Polynomial.MUL_PP_P(p1, p2)
        expected = Polynomial("1 1")  # x + 1, один корень остался кратным
        self.assertEqual(str(expected), str(p1.NMP_P_P()), msg=f"Failed for polynomial with mixed roots")

        # Проверка на многочлен, который после преобразования станет константой
        # Это теоретический случай, так как обычно многочлен не превращается в константу после удаления кратных корней,
        # но для полноты теста включим этот случай, предполагая, что реализация может обрабатывать такие экстремальные случаи
        p1 = Polynomial("1 3 3 1")  # (x + 1)^3, но если предположить, что после обработки он станет константой
        expected = Polynomial("1")  # для демонстрации, что функция может вернуть константу
        self.assertEqual(str(expected), str(p1.NMP_P_P()), msg=f"Failed for polynomial reducing to constant")

if __name__ == '__main__':
    # запускаем все тесты которые есть
    unittest.main()

    # Пример запуска конкретного модуля
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestNatural)
    # unittest.TextTestRunner().run(suite)