import unittest
from Natural import Natural
#from Integer import Integer
#from Rational import Rational
#from Polynomial import Polynomial


# Тесты класса натуральных
class TestNatural(unittest.TestCase):
    def test_init(self):
        # Лучший случай:
        n = Natural('5')
        self.assertEqual(n.number, [5], msg=f"Natural('5')")

        # Средний случай:
        n = Natural('123')
        self.assertEqual([1, 2, 3], n.number,  msg=f"Natural('123')")

        # Худший случай: число с ведущими нулями
        n = Natural('000123')
        self.assertEqual([1, 2, 3], n.number,  msg=f"Natural('0123')")

    def test_str(self):
        # Лучший случай:
        n = Natural('5')
        self.assertEqual('5', str(n),  msg=f"str(Natural('5'))")

        # Средний случай:
        n = Natural('123')
        self.assertEqual('123', str(n),  msg=f"str(Natural('123'))")

        # Худший случай:
        n = Natural('0123')
        self.assertEqual('123', str(n),  msg=f"str(Natural('0123'))")

    def test_COM_NN_D(self):
        # Худший случай: сравнение двух равных чисел
        n1 = Natural('123')
        n2 = Natural('123')
        self.assertEqual(0, n1.COM_NN_D(n2),  msg=f"COM_NN_D(Natural('123'), Natural('123'))")

        # Средний случай: сравнение двух неравных чисел
        n1 = Natural('123')
        n2 = Natural('456')
        self.assertEqual(1, n1.COM_NN_D(n2),  msg=f"COM_NN_D(Natural('123'), Natural('456'))")

        # Лучший случай: сравнение двух чисел с разной длиной
        n1 = Natural('123')
        n2 = Natural('1234')
        self.assertEqual(1, n1.COM_NN_D(n2), msg=f"COM_NN_D(Natural('123'), Natural('1234'))")

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
        self.assertEqual('124', str(n.ADD_1N_N()), msg=f"ADD_1N_N(Natural('123'))")

        # Средний случай: прибавление 1 к числу, оканчивающемуся на 9
        n = Natural('129')
        self.assertEqual('130', str(n.ADD_1N_N()), msg=f"ADD_1N_N(Natural('129'))")

        # Худший случай: прибавление 1 к числу, состоящему только из 9
        n = Natural('999')
        self.assertEqual('1000', str(n.ADD_1N_N()), msg=f"ADD_1N_N(Natural('999'))")

    def test_ADD_NN_N(self):
        # Лучший случай: сложение двух чисел без переноса
        n1 = Natural('123')
        n2 = Natural('456')
        self.assertEqual('579', str(n1.ADD_NN_N(n2)), msg=f"ADD_NN_N(Natural('123'), Natural('456'))")

        # Средний случай: сложение двух чисел с переносом
        n1 = Natural('129')
        n2 = Natural('456')
        self.assertEqual('585', str(n1.ADD_NN_N(n2)),  msg=f"ADD_NN_N(Natural('129'), Natural('456'))")

        # Худший случай: сложение двух чисел с разной длиной
        n1 = Natural('123')
        n2 = Natural('1234')
        self.assertEqual('1357',  str(n1.ADD_NN_N(n2)),  msg=f"ADD_NN_N(Natural('123'), Natural('1234')) ")

    def test_SUB_NN_N(self):
        # Лучший случай: без заема
        n1 = Natural('456')
        n2 = Natural('123')
        self.assertEqual('333', str(n1.SUB_NN_N(n2)), msg=f"SUB_NN_N(Natural('456'), Natural('123')) ")

        # Средний случай: с займом
        n1 = Natural('456')
        n2 = Natural('279')
        self.assertEqual('177', str(n1.SUB_NN_N(n2)),  msg=f"SUB_NN_N(Natural('456'), Natural('279')) ")

        # Худший случай: вычитание равных чисел
        n1 = Natural('123')
        n2 = Natural('123')
        self.assertEqual('0', str(n1.SUB_NN_N(n2)),  msg=f"SUB_NN_N(Natural('123'), Natural('123'))")

    def test_MUL_ND_N(self):
        # Лучший случай: умножение числа на 0
        n = Natural('123')
        self.assertEqual('0', str(n.MUL_ND_N(0)), msg=f"MUL_ND_N(Natural('123'), 0)")

        # Средний случай: умножение числа на цифру
        n = Natural('123')
        self.assertEqual('615', str(n.MUL_ND_N(5)),  msg=f"MUL_ND_N(Natural('123'), 5)")

        # Худший случай: умножение числа на 9
        n = Natural('123')
        self.assertEqual('1107', str(n.MUL_ND_N(9)), msg=f"MUL_ND_N(Natural('123'), 9)")

    def test_MUL_Nk_N(self):
        # Лучший случай: умножение числа на 10^0
        n = Natural('123')
        self.assertEqual('123', str(n.MUL_Nk_N(0)), msg=f"MUL_Nk_N(Natural('123'), 0)")

        # Средний случай: умножение числа на 10^k
        n = Natural('123')
        self.assertEqual('123000', str(n.MUL_Nk_N(3)),  msg=f"MUL_Nk_N(Natural('123'), 3)")

        # Худший случай: умножение числа на 10^10
        n = Natural('123')
        self.assertEqual('1230000000000', str(n.MUL_Nk_N(10)), msg=f"MUL_Nk_N(Natural('123'), 10)")

    def test_MUL_NN_N(self):
        # Лучший случай: умножение двух чисел, одно из которых 0
        n1 = Natural('123')
        n2 = Natural('0')
        self.assertEqual('0', str(n1.MUL_NN_N(n2)),  msg=f"MUL_NN_N(Natural('123'), Natural('0'))")

        # Средний случай: умножение двух чисел
        n1 = Natural('123')
        n2 = Natural('456')
        self.assertEqual('56088', str(n1.MUL_NN_N(n2)), msg=f"MUL_NN_N(Natural('123'), Natural('456'))")

        # Худший случай: умножение двух больших чисел
        n1 = Natural('123456')
        n2 = Natural('789012')
        self.assertEqual('97408265472', str(n1.MUL_NN_N(n2)), msg=f"MUL_NN_N(Natural('123456'), Natural('789012'))")

    def test_SUB_NDN_N(self):
        # Лучший случай: вычитание числа, умноженного на 0
        n1 = Natural('123')
        n2 = Natural('456')
        self.assertEqual('123', str(n1.SUB_NDN_N(n2, 0)), msg=f"SUB_NDN_N(Natural('123'), Natural('456'), 0)")

        # Средний случай: вычитание числа, умноженного на цифру
        n1 = Natural('123')
        n2 = Natural('45')
        self.assertEqual('33', str(n1.SUB_NDN_N(n2, 2)), msg=f"SUB_NDN_N(Natural('123'), Natural('45'), 2)")

        # Худший случай: вычитание числа, умноженного на 9
        n1 = Natural('123')
        n2 = Natural('10')
        self.assertEqual('33', str(n1.SUB_NDN_N(n2, 9)), msg=f"SUB_NDN_N(Natural('123'), Natural('10'), 9)")

    def test_DIV_NN_Dk(self):
        # Лучший случай: деление числа на 100
        n1 = Natural('123')
        n2 = Natural('1')
        self.assertEqual(1, n1.DIV_NN_Dk(n2, 2),  msg=f"DIV_NN_Dk(Natural('123'), Natural('1'), 2)")

        # Средний случай: деление числа на делитель
        n1 = Natural('123')
        n2 = Natural('12')
        self.assertEqual(1, n1.DIV_NN_Dk(n2, 1),  msg=f"DIV_NN_Dk(Natural('123'), Natural('12'), 1)")

    def test_DIV_NN_N(self):
        # Лучший случай: деление на 1
        n1 = Natural('123')
        n2 = Natural('1')
        self.assertEqual('123', str(n1.DIV_NN_N(n2)),  msg=f"DIV_NN_N(Natural('123'), Natural('1'))")

        # Средний случай: деление с остатком
        n1 = Natural('123')
        n2 = Natural('12')
        self.assertEqual('10', str(n1.DIV_NN_N(n2)),  msg=f"DIV_NN_N(Natural('123'), Natural('12'))")

        # Худший случай: деление на число большее
        n1 = Natural('123456')
        n2 = Natural('789012')
        self.assertEqual('0', str(n1.DIV_NN_N(n2)),  msg=f"DIV_NN_N(Natural('123456'), Natural('789012'))")

        # Деление на само себя
        n1 = Natural('123')
        n2 = Natural('123')
        self.assertEqual('1', str(n1.DIV_NN_N(n2)),  msg=f"DIV_NN_N(Natural('123'), Natural('123'))")

        # Деление на число, кратное данному
        n1 = Natural('246')
        n2 = Natural('123')
        self.assertEqual('2', str(n1.DIV_NN_N(n2)),  msg=f"DIV_NN_N(Natural('123'), Natural('246'))")

    def test_MOD_NN_N(self):
        # Лучший случай: остаток от деления числа на 1
        n1 = Natural('123')
        n2 = Natural('1')
        self.assertEqual('0', str(n1.MOD_NN_N(n2)), msg=f"MOD_NN_N(Natural('123'), Natural('1'))")

        # Средний случай: остаток от деления числа на делитель
        n1 = Natural('123')
        n2 = Natural('12')
        self.assertEqual('3', str(n1.MOD_NN_N(n2)), msg=f"MOD_NN_N(Natural('123'), Natural('12'))")

        # Худший случай: остаток от деления числа на большое число
        n1 = Natural('123456')
        n2 = Natural('789012')
        self.assertEqual('123456', str(n1.MOD_NN_N(n2)), msg=f"MOD_NN_N(Natural('123456'), Natural('78901'))")

        # Деление на само себя
        n1 = Natural('123')
        n2 = Natural('123')
        self.assertEqual('0', str(n1.MOD_NN_N(n2)), msg=f"MOD_NN_N(Natural('123'), Natural('123'))")

        # Деление на число, кратное данному
        n1 = Natural('123')
        n2 = Natural('246')
        self.assertEqual('123', str(n1.MOD_NN_N(n2)),  msg=f"MOD_NN_N(Natural('123'), Natural('246'))")

    def test_GCF_NN_N(self):
        # Лучший случай: НОД двух одинаковых чисел
        n1 = Natural('123')
        n2 = Natural('123')
        self.assertEqual('123', str(n1.GCF_NN_N(n2)), msg=f"GCF_NN_N(Natural('123'), Natural('123'))")

        # Средний случай: НОД двух разных чисел
        n1 = Natural('12')
        n2 = Natural('18')
        self.assertEqual('6', str(n1.GCF_NN_N(n2)), msg=f"GCF_NN_N(Natural('12'), Natural('18'))")

        # Худший случай: НОД двух больших чисел
        n1 = Natural('123456')
        n2 = Natural('789012')
        self.assertEqual('12', str(n1.GCF_NN_N(n2)), msg=f"GCF_NN_N(Natural('123456'), Natural('789012'))")

        # НОД числа и 1
        n1 = Natural('123')
        n2 = Natural('1')
        self.assertEqual('1', str(n1.GCF_NN_N(n2)), msg=f"GCF_NN_N(Natural('123'), Natural('1'))")

        # НОД числа и 0
        n1 = Natural('23')
        n2 = Natural('0')
        self.assertEqual('23', str(n1.GCF_NN_N(n2)), msg=f"GCF_NN_N(Natural('23'), Natural('0'))")

        # НОД двух простых чисел
        n1 = Natural('23')
        n2 = Natural('37')
        self.assertEqual('1', str(n1.GCF_NN_N(n2)), msg=f"GCF_NN_N(Natural('23'), Natural('37'))")

    def test_LCM_NN_N(self):
        # Лучший случай: НОК двух одинаковых чисел
        n1 = Natural('123')
        n2 = Natural('123')
        self.assertEqual('123', str(n1.LCM_NN_N(n2)), msg=f"Natural('123').LCM_NN_N(Natural('123'))")

        # Средний случай: НОК двух разных чисел
        n1 = Natural('12')
        n2 = Natural('18')
        self.assertEqual('36', str(n1.LCM_NN_N(n2)), msg=f"Natural('12').LCM_NN_N(Natural('18'))")


        # Худший случай: НОК двух больших чисел
        n1 = Natural('123456')
        n2 = Natural('789012')
        self.assertEqual('8117355456', str(n1.LCM_NN_N(n2)),  msg=f"Natural('123456').LCM_NN_N(Natural('789012'))")

        # НОК числа и 1
        n1 = Natural('123')
        n2 = Natural('1')
        self.assertEqual('123', str(n1.LCM_NN_N(n2)), msg=f"Natural('123').LCM_NN_N(Natural('1'))")

        # НОК двух простых чисел
        n1 = Natural('23')
        n2 = Natural('37')
        self.assertEqual('851', str(n1.LCM_NN_N(n2)), msg=f"Natural('23').LCM_NN_N(Natural('37'))")


if __name__ == '__main__':
    # запускаем все тесты которые есть
    unittest.main()

    # Пример запуска конкретного модуля
    #suite = unittest.TestLoader().loadTestsFromTestCase(TestNatural)
    #unittest.TextTestRunner().run(suite)