class Natural:
    def __init__(self, number: str):
        self.number = list(map(int, number))

    def __str__(self):
        return ''.join(map(str, self.number))



    # Сравнение натуральных чисел: 2 - если первое больше второго, 0, если равно, 1 иначе.
    def COM_NN_D(self, other):
        if len(self.number) > len(other.number): return 2
        elif len(self.number) < len(other.number): return 1
        else:
            for a, b in zip(self.number, other.number):
                if a > b:
                    return 2
                elif a < b:
                    return 1
            return 0

    # Проверка на ноль: если число не равно нулю, то «да» иначе «нет»
    def NZER_N_B(self):
        return self.number != [0]

    # Добавление 1 к натуральному числу
    def ADD_1N_N(self):
        result = Natural(str(self))
        carry = 1
        for i in range(len(result.number) - 1, -1, -1):
            if carry == 0: break
            result.number[i] += carry
            if result.number[i] == 10:
                result.number[i] = 0
                carry = 1
            else:
                carry = 0
        if carry == 1:
            result.number.insert(0, 1)
        return result

    # Сложение натуральных чисел
    def ADD_NN_N(self, other):
        result = []
        carry = 0
        max_len = max(len(self.number), len(other.number))
        for i in range(max_len):
            digit_a = self.number[-i-1] if i < len(self.number) else 0
            digit_b = other.number[-i-1] if i < len(other.number) else 0
            total = digit_a + digit_b + carry
            result.insert(0, total % 10)
            carry = total // 10
        if carry:
            result.insert(0, carry)

        return Natural(''.join(map(str, result)))

    # Вычитание из первого большего натурального числа второго меньшего или равного
    def SUB_NN_N(self, other):
        if self.COM_NN_D(other) == 1: # если второе больше первого
            raise ValueError("Cannot subtract a larger number from a smaller one")
        result = []
        borrow = 0
        for i in range(len(self.number)):
            digit_a = self.number[-i-1]
            digit_b = other.number[-i-1] if i < len(other.number) else 0
            if digit_a < digit_b + borrow:
                result.insert(0, digit_a + 10 - digit_b - borrow)
                borrow = 1
            else:
                result.insert(0, digit_a - digit_b - borrow)
                borrow = 0

        # Удаляем ведущие нули
        while len(result) > 1 and result[0] == 0:
            result.pop(0)
        return Natural(''.join(map(str, result)))

    # Умножение натурального числа на цифру
    def MUL_ND_N(self, digit):
        if not (0 <= digit <= 9):
            raise ValueError("Digit must be between 0 and 9")
        result = []
        carry = 0
        for i in range(len(self.number) - 1, -1, -1):
            total = self.number[i] * digit + carry
            result.insert(0, total % 10)
            carry = total // 10
        while carry:
            result.insert(0, carry % 10)
            carry //= 10

        return Natural(''.join(map(str, result)))

    # Умножение натурального числа на 10^k, k-натуральное
    def MUL_Nk_N(self, k):
        if k < 0:
            raise ValueError("k must be a non-negative integer")
        return Natural(str(self) + '0' * k)

    # Умножение натуральных чисел
    def MUL_NN_N(self, other):
        result = Natural('0')
        for i in range(len(other.number)):
            digit = other.number[-i-1]
            temp_result = self.MUL_ND_N(digit).MUL_Nk_N(i)
            result = result.ADD_NN_N(temp_result)
        return result

    # Вычитание из натурального другого натурального, умноженного на цифру для случая с неотрицательным результатом
    def SUB_NDN_N(self, other, digit):
        return self.SUB_NN_N(other.MUL_ND_N(digit))

    # Вычисление первой цифры деления большего натурального на меньшее, домноженное на 10^k, где k - номер позиции этой цифры (номер считается с нуля)
    def DIV_NN_Dk(self, other, k):
        if other.COM_NN_D(self) == 2:
            raise ValueError("Cannot divide a larger number by a smaller one")
        divisor = other.MUL_Nk_N(k)
        for i in range(10):
            if divisor.MUL_ND_N(i).COM_NN_D(self) == 2:
                return i - 1
        return 9

    # Неполное частное от деления первого натурального числа на второе с остатком (делитель отличен от нуля)
    def DIV_NN_N(self, other):
        quotient = Natural('0')
        remainder = Natural(str(self))
        while remainder.COM_NN_D(other) == 2 or remainder.COM_NN_D(other) == 0:
            remainder = remainder.SUB_NN_N(other)
            quotient = quotient.ADD_1N_N()
        return quotient

    # Остаток от деления первого натурального числа на второе натуральное (делитель отличен от нуля)
    def MOD_NN_N(self, other):
        if self.COM_NN_D(other) == 1: return self
        quotient = self.DIV_NN_N(other)
        return self.SUB_NN_N(quotient.MUL_NN_N(other))

    # НОД натуральных чисел
    def GCF_NN_N(self, other):
        a = Natural(str(self))
        b = Natural(str(other))
        if self.COM_NN_D(other) == 2: a,b = b,a
        while a.NZER_N_B() and b.NZER_N_B():
            a, b = b, a.MOD_NN_N(b)
        return a

    # НОК натуральных чисел
    def LCM_NN_N(self, other):
        return self.MUL_NN_N(other).DIV_NN_N(self.GCF_NN_N(other))



# Тестики (нужно допилить)
def Natural_tests():
    num1 = Natural("123")
    num2 = Natural("456")
    num3 = Natural("1000")
    num4 = Natural("999")
    num5 = Natural("0")
    num6 = Natural("2000")
    def test_COM_NN_D():
        print("Сравнение:")
        print(f"{num1} < {num2}: {num1.COM_NN_D(num2)}")  # 1
        print(f"{num2} > {num1}: {num2.COM_NN_D(num1)}")  # 2
        print(f"{num1} == {num1}: {num1.COM_NN_D(num1)}")  # 0
        print()
    def test_NZER_N_B():
        print("Проверка на ноль:")
        print(f"{num1} != 0: {num1.NZER_N_B()}")       # True
        print(f"{num5} != 0: {num5.NZER_N_B()}")       # False
        print()
    def test_ADD_NN_N():
        print("Сложение:")
        print(f"{num1} + 1 = {num1.ADD_1N_N()}")       # 124
        print(f"{num2} + 1 = {num2.ADD_1N_N()}")       # 457
        print(f"{num3} + 1 = {num3.ADD_1N_N()}")       # 1001
        print(f"{num3} + {num2} = {num3.ADD_NN_N(num2)}")   # 1456
        print()
    def test_SUB_NN_N():
        print("Вычитание:")
        print(f"{num3} - {num2} = {num3.SUB_NN_N(num2)}")   # 544
        print()
    def test_MUL_NN_N():
        print("Умножение:")
        print(f"{num1} * 2 = {num1.MUL_ND_N(2)}")      # 246
        print(f"{num1} * 9 = {num1.MUL_ND_N(9)}")      # 1107
        print(f"{num1} * 10^3 = {num1.MUL_Nk_N(3)}")  # 123000
        print(f"{num1} * 10^0 = {num1.MUL_Nk_N(0)}")  # 123
        print(f"{num1} * {num3} = {num1.MUL_NN_N(num3)}")   # 123000
        print(f"{num1} * {num2} = {num1.MUL_NN_N(num2)}")   # 56088
        print()
    def test_SUB_NDN_N():
        print("Вычитание с умножением:")
        print(f"{num3} - ({num1} * 2) = {num3.SUB_NDN_N(num1, 2)}")  # 754
        print(f"{num3} - ({num4} * 1) = {num3.SUB_NDN_N(num4, 1)}")  # 1
        print()
    def test_DIV_NN_N():
        print("Деление:")
        print(f"{num3} // {num1} = {num3.DIV_NN_N(num1)}")   # 8
        print(f"{num3} // {num3} = {num3.DIV_NN_N(num3)}")   # 1
        print(f"{num6} // {num3} = {num6.DIV_NN_N(num3)}")   # 2
        print()
    def test_MOD_NN_N():
        print("Остаток от деления:")
        print(f"{num3} % {num1} = {num3.MOD_NN_N(num1)}")   # 16
        print(f"{num3} % {num3} = {num3.MOD_NN_N(num3)}")   # 0
        print(f"{num1} % {num3} = {num1.MOD_NN_N(num3)}")   # 123
        print()
    def test_GCF_NN_N():
        print("Наибольший общий делитель (НОД):")
        print(f"НОД({num2}, {num3}) = {num2.GCF_NN_N(num3)}")   # 8
        print()
    def test_LCM_NN_N():
        print("Наименьшее общее кратное (НОК):")
        print(f"НОК({num2}, {num3}) = {num2.LCM_NN_N(num3)}")   # 57000
    print("\n______ПРОВЕРКА НАТУРАЛЬНЫХ______\n")
    test_COM_NN_D()
    test_NZER_N_B()
    test_ADD_NN_N()
    test_SUB_NN_N()
    test_MUL_NN_N()
    test_SUB_NDN_N()
    test_DIV_NN_N()
    test_MOD_NN_N()
    test_GCF_NN_N()
    test_LCM_NN_N()



if __name__ == '__main__':
    Natural_tests()



