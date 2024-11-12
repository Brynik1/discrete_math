import unittest
from modules.Natural import Natural
from modules.Integer import Integer
from modules.Rational import Rational
from modules.Polynomial import Polynomial


# Тесты класса натуральных
class TestNatural(unittest.TestCase):
    def test_init(self):
        # Лучший случай:
        n = Natural('5')
        self.assertEqual(n.number, [5], msg=f"Natural('5')")

        # Средний случай:
        n = Natural('123')
        self.assertEqual([1, 2, 3], n.number, msg=f"Natural('123')")

        # Худший случай: число с ведущими нулями
        n = Natural('000123')
        self.assertEqual([1, 2, 3], n.number, msg=f"Natural('0123')")

    def test_str(self):
        # Лучший случай:
        n = Natural('5')
        self.assertEqual('5', str(n), msg=f"str(Natural('5'))")

        # Средний случай:
        n = Natural('123')
        self.assertEqual('123', str(n), msg=f"str(Natural('123'))")

        # Худший случай:
        n = Natural('0123')
        self.assertEqual('123', str(n), msg=f"str(Natural('0123'))")

    def test_COM_NN_D(self):
        # Худший случай: сравнение двух равных чисел
        n1 = Natural('123')
        n2 = Natural('123')
        self.assertEqual(0, n1.COM_NN_D(n2), msg=f"COM_NN_D(Natural('123'), Natural('123'))")

        # Средний случай: сравнение двух неравных чисел
        n1 = Natural('123')
        n2 = Natural('456')
        self.assertEqual(1, n1.COM_NN_D(n2), msg=f"COM_NN_D(Natural('123'), Natural('456'))")

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
        self.assertEqual('585', str(n1.ADD_NN_N(n2)), msg=f"ADD_NN_N(Natural('129'), Natural('456'))")

        # Худший случай: сложение двух чисел с разной длиной
        n1 = Natural('123')
        n2 = Natural('1234')
        self.assertEqual('1357', str(n1.ADD_NN_N(n2)), msg=f"ADD_NN_N(Natural('123'), Natural('1234')) ")

    def test_SUB_NN_N(self):
        # Лучший случай: без заема
        n1 = Natural('456')
        n2 = Natural('123')
        self.assertEqual('333', str(n1.SUB_NN_N(n2)), msg=f"SUB_NN_N(Natural('456'), Natural('123')) ")

        # Средний случай: с займом
        n1 = Natural('456')
        n2 = Natural('279')
        self.assertEqual('177', str(n1.SUB_NN_N(n2)), msg=f"SUB_NN_N(Natural('456'), Natural('279')) ")

        # Худший случай: вычитание равных чисел
        n1 = Natural('123')
        n2 = Natural('123')
        self.assertEqual('0', str(n1.SUB_NN_N(n2)), msg=f"SUB_NN_N(Natural('123'), Natural('123'))")

    def test_MUL_ND_N(self):
        # Лучший случай: умножение числа на 0
        n = Natural('123')
        self.assertEqual('0', str(n.MUL_ND_N(0)), msg=f"MUL_ND_N(Natural('123'), 0)")

        # Средний случай: умножение числа на цифру
        n = Natural('123')
        self.assertEqual('615', str(n.MUL_ND_N(5)), msg=f"MUL_ND_N(Natural('123'), 5)")

        # Худший случай: умножение числа на 9
        n = Natural('123')
        self.assertEqual('1107', str(n.MUL_ND_N(9)), msg=f"MUL_ND_N(Natural('123'), 9)")

    def test_MUL_Nk_N(self):
        # Лучший случай: умножение числа на 10^0
        n = Natural('123')
        self.assertEqual('123', str(n.MUL_Nk_N(0)), msg=f"MUL_Nk_N(Natural('123'), 0)")

        # Средний случай: умножение числа на 10^k
        n = Natural('123')
        self.assertEqual('123000', str(n.MUL_Nk_N(3)), msg=f"MUL_Nk_N(Natural('123'), 3)")

        # Худший случай: умножение числа на 10^10
        n = Natural('123')
        self.assertEqual('1230000000000', str(n.MUL_Nk_N(10)), msg=f"MUL_Nk_N(Natural('123'), 10)")

    def test_MUL_NN_N(self):
        # Лучший случай: умножение двух чисел, одно из которых 0
        n1 = Natural('123')
        n2 = Natural('0')
        self.assertEqual('0', str(n1.MUL_NN_N(n2)), msg=f"MUL_NN_N(Natural('123'), Natural('0'))")

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
        self.assertEqual(1, n1.DIV_NN_Dk(n2, 2), msg=f"DIV_NN_Dk(Natural('123'), Natural('1'), 2)")

        # Средний случай: деление числа на делитель
        n1 = Natural('123')
        n2 = Natural('12')
        self.assertEqual(1, n1.DIV_NN_Dk(n2, 1), msg=f"DIV_NN_Dk(Natural('123'), Natural('12'), 1)")

    def test_DIV_NN_N(self):
        # Лучший случай: деление на 1
        n1 = Natural('123')
        n2 = Natural('1')
        self.assertEqual('123', str(n1.DIV_NN_N(n2)), msg=f"DIV_NN_N(Natural('123'), Natural('1'))")

        # Средний случай: деление с остатком
        n1 = Natural('123')
        n2 = Natural('12')
        self.assertEqual('10', str(n1.DIV_NN_N(n2)), msg=f"DIV_NN_N(Natural('123'), Natural('12'))")

        # Худший случай: деление на число большее
        n1 = Natural('123456')
        n2 = Natural('789012')
        self.assertEqual('0', str(n1.DIV_NN_N(n2)), msg=f"DIV_NN_N(Natural('123456'), Natural('789012'))")

        # Деление на само себя
        n1 = Natural('123')
        n2 = Natural('123')
        self.assertEqual('1', str(n1.DIV_NN_N(n2)), msg=f"DIV_NN_N(Natural('123'), Natural('123'))")

        # Деление на число, кратное данному
        n1 = Natural('246')
        n2 = Natural('123')
        self.assertEqual('2', str(n1.DIV_NN_N(n2)), msg=f"DIV_NN_N(Natural('123'), Natural('246'))")

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
        self.assertEqual('123', str(n1.MOD_NN_N(n2)), msg=f"MOD_NN_N(Natural('123'), Natural('246'))")

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
        self.assertEqual('8117355456', str(n1.LCM_NN_N(n2)), msg=f"Natural('123456').LCM_NN_N(Natural('789012'))")

        # НОК числа и 1
        n1 = Natural('123')
        n2 = Natural('1')
        self.assertEqual('123', str(n1.LCM_NN_N(n2)), msg=f"Natural('123').LCM_NN_N(Natural('1'))")

        # НОК двух простых чисел
        n1 = Natural('23')
        n2 = Natural('37')
        self.assertEqual('851', str(n1.LCM_NN_N(n2)), msg=f"Natural('23').LCM_NN_N(Natural('37'))")


# Тесты класса целых
class TestInteger(unittest.TestCase):
    def test_ABS_Z_N(self):
        # Лучший случай: положительное число
        a = Integer('12345')
        self.assertEqual('12345', str(a.ABS_Z_N()), msg=f"Integer('12345').ABS_Z_N()")

        # Средний случай: отрицательное число
        a = Integer('-12345')
        self.assertEqual('12345', str(a.ABS_Z_N()), msg=f"Integer('-12345').ABS_Z_N()")

        # Крайний случай: ноль
        a = Integer('0')
        self.assertEqual('0', str(a.ABS_Z_N()), msg=f"Integer('0').ABS_Z_N()")

    def test_POZ_Z_D(self):
        # Лучший случай: положительное число
        a = Integer('12345')
        self.assertEqual(2, a.POZ_Z_D(), msg="Integer('12345').POZ_Z_D()")

        # Средний случай: отрицательное число
        a = Integer('-12345')
        self.assertEqual(1, a.POZ_Z_D(), msg="Integer('-12345').POZ_Z_D()")

        # Крайний случай: ноль
        a = Integer('0')
        self.assertEqual(0, a.POZ_Z_D(), msg="Integer('0').POZ_Z_D()")

    def test_MUL_ZM_Z(self):
        # Лучший случай: положительное число
        a = Integer('12345')
        self.assertEqual('-12345', str(a.MUL_ZM_Z()), msg="Integer('12345').MUL_ZM_Z()")

        # Средний случай: отрицательное число
        a = Integer('-12345')
        self.assertEqual('12345', str(a.MUL_ZM_Z()), msg="Integer('-12345').MUL_ZM_Z()")

        # Крайний случай: ноль
        a = Integer('0')
        expected = '0'
        self.assertEqual(expected, str(a.MUL_ZM_Z()), msg="Integer('0').MUL_ZM_Z()")

    def test_TRANS_N_Z(self):
        # Лучший случай: натуральное число
        a = Natural('12345')
        self.assertEqual('12345', str(Integer.TRANS_N_Z(a)), msg="Integer.TRANS_N_Z(Natural('12345'))")

        # Крайний случай: ноль
        a = Natural('0')
        self.assertEqual('0', str(Integer.TRANS_N_Z(a)), msg="Integer.TRANS_N_Z(Natural('0'))")

    def test_TRANS_Z_N(self):
        # Лучший случай: положительное число
        a = Integer('12345')
        self.assertEqual('12345', str(a.TRANS_Z_N()), msg="Integer('12345').TRANS_Z_N()")

        # Худший случай: отрицательное число
        a = Integer('-12345')
        self.assertEqual('12345', str(a.TRANS_Z_N()), msg="Integer('-12345').TRANS_Z_N()")

        # Крайний случай: ноль
        a = Integer('0')
        self.assertEqual('0', str(a.TRANS_Z_N()), msg="Integer('0').TRANS_Z_N()")

    def test_ADD_ZZ_Z(self):
        # Лучший случай: сложение положительных чисел
        a = Integer('12345')
        b = Integer('67890')
        self.assertEqual('80235', str(a.ADD_ZZ_Z(b)), msg="Integer('12345').ADD_ZZ_Z(Integer('67890'))")

        # Средний случай: сложение отрицательных чисел
        a = Integer('-12345')
        b = Integer('-67890')
        self.assertEqual('-80235', str(a.ADD_ZZ_Z(b)), msg="Integer('-12345').ADD_ZZ_Z(Integer('-67890'))")

        # Худший случай: сложение чисел с разными знаками
        a = Integer('12345')
        b = Integer('-67890')
        self.assertEqual('-55545', str(a.ADD_ZZ_Z(b)), msg="Integer('12345').ADD_ZZ_Z(Integer('-67890'))")

        # Крайний случай 1: сложение с нулем
        a = Integer('12345')
        b = Integer('0')
        self.assertEqual('12345', str(a.ADD_ZZ_Z(b)), msg="Integer('12345').ADD_ZZ_Z(Integer('0'))")

        # Крайний случай 2: сложение равных по модулю, но разных по знаку чисел
        a = Integer('12345')
        b = Integer('-12345')
        self.assertEqual('0', str(a.ADD_ZZ_Z(b)), msg="Integer('12345').ADD_ZZ_Z(Integer('-12345'))")

    def test_SUB_ZZ_Z(self):
        # Лучший случай: вычитание положительных чисел
        a = Integer('12345')
        b = Integer('67890')
        self.assertEqual('-55545', str(a.SUB_ZZ_Z(b)), msg="12345 - 67890")

        # Средний случай: вычитание отрицательных чисел
        a = Integer('-12345')
        b = Integer('-67890')
        self.assertEqual('55545', str(a.SUB_ZZ_Z(b)), msg="-12345 - -67890")

        # Худший случай: вычитание чисел с разными знаками
        a = Integer('12345')
        b = Integer('-67890')
        self.assertEqual('80235', str(a.SUB_ZZ_Z(b)), msg="12345 - -67890")

        # Крайний случай: вычитание нуля
        a = Integer('12345')
        b = Integer('0')
        self.assertEqual('12345', str(a.SUB_ZZ_Z(b)), msg="12345 - 0")

        # Крайний случай: вычитание из нуля
        a = Integer('0')
        b = Integer('12345')
        self.assertEqual('-12345', str(a.SUB_ZZ_Z(b)), msg="0 - 12345")

    def test_MUL_ZZ_Z(self):
        # Лучший случай: умножение положительных чисел
        a = Integer('12345')
        b = Integer('67890')
        self.assertEqual('838102050', str(a.MUL_ZZ_Z(b)), msg="12345 * 67890")

        # Средний случай: умножение отрицательных чисел
        a = Integer('-12345')
        b = Integer('-67890')
        self.assertEqual('838102050', str(a.MUL_ZZ_Z(b)), msg="-12345 * -67890")

        # Худший случай: умножение чисел с разными знаками
        a = Integer('12345')
        b = Integer('-67890')
        self.assertEqual('-838102050', str(a.MUL_ZZ_Z(b)), msg="12345 * -67890")

        # Крайний случай: умножение на ноль
        a = Integer('12345')
        b = Integer('0')
        self.assertEqual('0', str(a.MUL_ZZ_Z(b)), msg="12345 * 0")

    def test_DIV_ZZ_Z(self):
        # Лучший случай: деление положительных чисел
        a = Integer('12345')
        b = Integer('123')
        self.assertEqual('100', str(a.DIV_ZZ_Z(b)), msg="12345 // 123")

        # Средний случай: деление отрицательных чисел
        a = Integer('-12345')
        b = Integer('-123')
        self.assertEqual('101', str(a.DIV_ZZ_Z(b)), msg="-12345 // -123")

        # Худший случай: деление чисел с разными знаками
        a = Integer('12345')
        b = Integer('-123')
        self.assertEqual('-100', str(a.DIV_ZZ_Z(b)), msg="12345 // -123")

        # Крайний случай: деление на единицу
        a = Integer('12345')
        b = Integer('1')
        self.assertEqual('12345', str(a.DIV_ZZ_Z(b)), msg="12345 // 1")

    def test_MOD_ZZ_Z(self):
        # Лучший случай: деление без остатка
        a = Integer('12345')
        b = Integer('12345')
        self.assertEqual('0', str(a.MOD_ZZ_Z(b)), msg="12345 % 12345")

        # Средний случай: деление с остатком
        a = Integer('12345')
        b = Integer('123')
        self.assertEqual('45', str(a.MOD_ZZ_Z(b)), msg="12345 % 123")

        # Худший случай: деление на отрицательное число
        a = Integer('12345')
        b = Integer('-123')
        self.assertEqual('45', str(a.MOD_ZZ_Z(b)), msg="12345 % -123")

        # Крайний случай: деление на единицу
        a = Integer('12345')
        b = Integer('1')
        self.assertEqual('0', str(a.MOD_ZZ_Z(b)), msg="12345 % 1")


# Тесты класса рациональных
class TestRational(unittest.TestCase):
    def test_init(self):
        # Лучший случай: корректное рациональное число
        a = Rational('123/456')
        self.assertEqual('123', str(a.numerator))
        self.assertEqual('456', str(a.denominator))

        # Средний случай: рациональное число с разделителем '|'
        a = Rational('123|456')
        self.assertEqual('123', str(a.numerator))
        self.assertEqual('456', str(a.denominator))

        # Средний случай: рациональное число с разделителем ':'
        a = Rational('123:456')
        self.assertEqual('123', str(a.numerator))
        self.assertEqual('456', str(a.denominator))

        # Средний случай: целое число
        a = Rational('123')
        self.assertEqual('123', str(a.numerator))
        self.assertEqual('1', str(a.denominator))

        # Крайний случай: ноль
        a = Rational('0')
        self.assertEqual('0', str(a.numerator))
        self.assertEqual('1', str(a.denominator))

    # ниже поменять надо местами первый и второй аргумент ассерта.   - Выполнено
    # Тк в случае неудачи он вывод как 1е ожидаемое, 2е полученное
    def test_str(self):
        # Лучший случай: рациональное число
        a = Rational('123/456')
        self.assertEqual('123/456', str(a))

        # Средний случай: целое число
        a = Rational('123/1')
        self.assertEqual('123', str(a))

        # Крайний случай: ноль
        a = Rational('0/1')
        self.assertEqual('0', str(a))

    def test_RED_Q_Q(self):
        # Лучший случай: несократимая дробь
        a = Rational('123/457')
        expected = Rational('123/457')
        self.assertEqual(str(expected), str(a.RED_Q_Q()))

        # Средний случай: сократимая дробь
        a = Rational('120/360')
        expected = Rational('1/3')
        self.assertEqual(str(expected), str(a.RED_Q_Q()))

        # Крайний случай: ноль
        a = Rational('0/123')
        expected = Rational('0/1')
        self.assertEqual(str(expected), str(a.RED_Q_Q()))

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
        self.assertEqual(str(expected), str(Rational.TRANS_Z_Q(a)))

        # Средний случай: отрицательное целое число
        a = Integer('-123')
        expected = Rational('-123/1')
        self.assertEqual(str(expected), str(Rational.TRANS_Z_Q(a)))

        # Крайний случай: ноль
        a = Integer('0')
        expected = Rational('0/1')
        self.assertEqual(str(expected), str(Rational.TRANS_Z_Q(a)))

    def test_TRANS_Q_Z(self):
        # Лучший случай: целое число
        a = Rational('123/1')
        expected = Integer('123')
        self.assertEqual(str(expected), str(a.TRANS_Q_Z()))

        # Средний случай: отрицательное целое число
        a = Rational('-123/1')
        expected = Integer('-123')
        self.assertEqual(str(expected), str(a.TRANS_Q_Z()))

        # Крайний случай: ноль
        a = Rational('0/1')
        expected = Integer('0')
        self.assertEqual(str(expected), str(a.TRANS_Q_Z()))


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
        self.assertEqual(str(expected), str(p1.ADD_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

        # Крайний случай: сложение одного многочлена с нулем
        p1 = Polynomial("1 2/3")
        p2 = Polynomial("0")
        expected = Polynomial("1 2/3")
        self.assertEqual(str(expected), str(p1.ADD_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

    def test_SUB_PP_P(self):
        # Лучший случай: вычитание двух многочленов без нулевых коэффициентов
        p1 = Polynomial("1 2/3")
        p2 = Polynomial("4 5/6")
        expected = Polynomial("-3 -1/6")
        self.assertEqual(str(expected), str(p1.SUB_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

        # Средний случай: вычитание многочленов с нулевыми коэффициентами
        p1 = Polynomial("1 0 2/3 0")
        p2 = Polynomial("0 4 0 5/6")
        expected = Polynomial("1 -4 2/3 -5/6")
        self.assertEqual(str(expected), str(p1.SUB_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

        # Крайний случай: вычитание одного многочлена с нулем
        p1 = Polynomial("1 2/3")
        p2 = Polynomial("0")
        expected = Polynomial("1 2/3")
        self.assertEqual(str(expected), str(p1.SUB_PP_P(p2)), msg=f"Failed for inputs {p1} and {p2}")

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
        p1 = Polynomial("1")
        expected = Rational("1")
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

        # Смешанные случаи
        p1 = Polynomial("1 1")
        expected = Rational("1/1")  # НОД(1, 1) = 1, НОК(1, 1) = 1
        self.assertEqual(str(expected), str(p1.FAC_P_Q()), msg=f"Failed for polynomial {p1}")

        p1 = Polynomial("1/2 1/3 1/4")
        expected = Rational("1/12")  # НОД(1, 1, 1) = 1, НОК(2, 3, 4) = 12
        self.assertEqual(str(expected), str(p1.FAC_P_Q()), msg=f"Failed for polynomial {p1}")

        p1 = Polynomial("0 0 0")
        expected = Rational("1/1")  # НОД(0, 0, 0) = 1, НОК(1, 1, 1) = 1
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
        expected = Polynomial("3 -3 1")  # (x^2 - 3x + 3).
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

        # Случай с большими числами 1
        p1 = Polynomial('-35/1 -33/1 -62/1 22/1')  # 22x^3 - 62x^2 - 33x -35
        p2 = Polynomial('207/121 51/22 1207/242')  # 1207/242x^2 + 51/22x + 207/121
        expected = Polynomial("-7243 -4941")  # НОД() = -4941x - 7243
        self.assertEqual(str(expected), str(p1.GCF_PP_P(p2)), msg=f"Failed for polynomial and its derivative")

        # Случай с большими числами 2
        p1 = Polynomial('-345 33/2 13/3 54/7')  # 22x^3 - 62x^2 - 33x -35
        p2 = Polynomial('534/4 -45/23 -76/5')  # 1207/242x^2 + 51/22x + 207/121
        expected = Polynomial("-6751544545 1792867542")  # НОД() = 1792867542x - 6751544545
        self.assertEqual(str(expected), str(p1.GCF_PP_P(p2)), msg=f"Failed for polynomial and its derivative")

        # Случай с большой степенью
        p1 = Polynomial('1 3 3 5 17')  # 17x^4 + 5x^3 + 3x^2 + 3x + 1
        p2 = Polynomial('3 0 0 34 24')  # 24x^4 + 34x^3 + 3
        expected = Polynomial("-25871 -12715")  # НОД() = -12715x -25871
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

        p1 = Polynomial("0 0 0 1")  # x^3
        expected = Polynomial("0 0 3")  # 3x^2
        self.assertEqual(str(expected), str(p1.DER_P_P()), msg=f"Failed for polynomial x^3")

    def test_NMP_P_P(self):
        # Лучший случай: многочлен с кратными корнями
        p1 = Polynomial("1 4 6 4 1")  # (x + 1)^4
        expected = Polynomial("1 1")  # x + 1, после преобразования кратные корни становятся простыми
        self.assertEqual(str(expected), str(p1.NMP_P_P()), msg=f"Failed for polynomial {p1}")

        # Случай, когда многочлен уже имеет простые корни
        p1 = Polynomial("1 3 3 1")  # (x + 1)^3,
        expected = Polynomial("1 1")
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
        expected = Polynomial("1 2 2 1")  # x^3 + 2x^2 + 2x + 1
        self.assertEqual(str(expected), str(p1.NMP_P_P()), msg=f"Failed for polynomial with mixed roots")

        p1 = Polynomial("1 3 3 1")  # (x + 1)^3
        expected = Polynomial("1 1")  # x + 1
        self.assertEqual(str(expected), str(p1.NMP_P_P()), msg=f"Failed for polynomial reducing to constant")


if __name__ == '__main__':
    # запускаем все тесты которые есть
    unittest.main()

    # Пример запуска конкретного модуля
    # suite = unittest.TestLoader().loadTestsFromTestCase(TestNatural)
    # unittest.TextTestRunner().run(suite)