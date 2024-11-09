class Natural:
    def __init__(self, number: str):
        number = list(map(int, number))
        while len(number) > 1 and number[0] == 0:           #вырезаем незначащие нули в числе
            number = number[1:]
        self.number = number

    def __str__(self):
        return ''.join(map(str, self.number))



    # Сравнение натуральных чисел: 2 - если первое больше второго, 0, если равно, 1 иначе.
    def COM_NN_D(self, other):
        if len(self.number) > len(other.number): return 2           #сравниваем значения по длине
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
        carry = 1           # carry будет использоваться для отслеживания переноса, если при сложении произойдет переход через 10
        for i in range(len(result.number) - 1, -1, -1):         #проходим по каждой цифре числа result справа налево (начиная с младшего разряда)
            if carry == 0: break            #добавляем значение carry к текущей цифре числа result
            result.number[i] += carry       #проверяем, если сумма цифры и переноса привела к значению 10, то текущий разряд обнуляется, а перенос устанавливается в 1 для передачи на следующий разряд
            if result.number[i] == 10:
                result.number[i] = 0
                carry = 1
            else:
                carry = 0
        if carry == 1:        #После завершения цикла проверяем, остался ли перенос, это может произойти, если после прибавления 1 все разряды стали нулями
            result.number.insert(0, 1)          #если carry равен 1, добавляем 1 в начало result
        return result

    # Сложение натуральных чисел
    def ADD_NN_N(self, other):
        x=self.COM_NN_D(Natural('0'))
        y=other.COM_NN_D(Natural('0'))
        if x==0 and y==0: #если оба числа нули
            return Natural('0')
        if x==0: #если одного число ноль
            return Natural(str(other))
        if y==0: #если второе число ноль
            return Natural(str(self))
        result = []
        carry = 0       #перенос
        max_len = max(len(self.number), len(other.number))      #определяем максимальную длину из двух чисел, чтобы обработать все разряды обоих чисел
        for i in range(max_len):
            #если индекс i меньше длины числа, берется цифра из числа, Если наоборот, берется 0
            digit_a = self.number[-i-1] if i < len(self.number) else 0
            digit_b = other.number[-i-1] if i < len(other.number) else 0
            total = digit_a + digit_b + carry       #складываем текущие цифры digit_a и digit_b, а также значение carry
            result.insert(0, total % 10)    #вставляем в начало списка последнюю цифру результата сложения разряда
            carry = total // 10         #обновляем carry для следующего разряда, разделив total на 10
        if carry:       #если после завершения цикла carry все еще не равен 0, добавляем его в начало result
            result.insert(0, carry)

        return Natural(''.join(map(str, result)))

    # Вычитание из первого большего натурального числа второго меньшего или равного
    def SUB_NN_N(self, other):
        if self.COM_NN_D(other) == 1: # если второе больше первого
            raise ValueError("Cannot subtract a larger number from a smaller one")
        result = []
        borrow = 0
        for i in range(len(self.number)):
            #Извлекаем цифру digit_a из числа self и digit_b из other:
            #digit_a всегда берется с конца, так как self длиннее или равен other.
            #Если индекс i превышает длину other, digit_b приравнивается к 0, для разности чисел разной длины.
            digit_a = self.number[-i-1]
            digit_b = other.number[-i-1] if i < len(other.number) else 0
            #Если digit_a меньше суммы digit_b и borrow, нужно занять 1 из следующего разряда:
            #К digit_a прибавляется 10, чтобы выполнить вычитание.
            #Borrow устанавливается в 1, чтобы учесть заем в следующем разряде
            if digit_a < digit_b + borrow:
                result.insert(0, digit_a + 10 - digit_b - borrow)
                borrow = 1
            else:       #Если digit_a больше или равен digit_b + borrow, заем не требуется:
                result.insert(0, digit_a - digit_b - borrow)        #Вычисляем разницу digit_a - digit_b - borrow
                borrow = 0
        # Удаляем ведущие нули
        while len(result) > 1 and result[0] == 0:
            result.pop(0)
        return Natural(''.join(map(str, result)))

    # Умножение натурального числа на цифру
    def MUL_ND_N(self, digit):
        if not (0 <= digit <= 9):       #если число не в нужном диапазоне
            print(digit)
            raise ValueError("Digit must be between 0 and 9")
        if digit==0 or self.COM_NN_D(Natural('0'))==0:      #если одно из чисел равно нулю
            return Natural('0')
        result = []
        carry = 0
        for i in range(len(self.number) - 1, -1, -1):
            total = self.number[i] * digit + carry
            result.insert(0, total % 10)
            carry = total // 10
        while carry:
            result.insert(0, carry % 10)
            carry //= 10        #Обновляем carry, взяв оставшуюся часть (total // 10). Она будет перенесена в следующий разряд.
        # Удаляем ведущие нули
        while len(result) > 1 and result[0] == 0:
            result.pop(0)
        return Natural(''.join(map(str, result)))

    # Умножение натурального числа на 10^k, k-натуральное
    def MUL_Nk_N(self, k):
        if k < 0:
            raise ValueError("k must be a non-negative integer")
        return Natural(str(self) + '0' * k)         #приписываем k нулей к строке

    # Умножение натуральных чисел
    def MUL_NN_N(self, other):
        x=self.COM_NN_D(Natural('1'))
        y=other.COM_NN_D(Natural('1'))
        if self.COM_NN_D(Natural('0'))==0 or other.COM_NN_D(Natural('0'))==0:       #если одно из чисел равно нулю
            return Natural('0')
        if x==0 and y==0:       #если оба числа равны единице
            return Natural('1')
        if x==0:    #если первое число равно единице
            return Natural(str(other))
        if y==0:    #если второе число равно единице
            return Natural(str(self))
        result = Natural('0')
        for i in range(len(other.number)):
            digit = other.number[-i-1]      #берем последнюю цифру второго числа
            temp_result = self.MUL_ND_N(digit).MUL_Nk_N(i)      #умножаем на цифру и результат умножения смещается на i разрядов влево, чтобы учесть позицию разряда digit в числе other
            result = result.ADD_NN_N(temp_result)
        return result

    # Вычитание из натурального другого натурального, умноженного на цифру для случая с неотрицательным результатом
    def SUB_NDN_N(self, other, digit):
        x=self.COM_NN_D(Natural('0'))
        y = other.COM_NN_D(Natural('0'))
        if digit==0 or y==0:    #если второе число или digit равны нулю
            return Natural(str(self))
        if x==0 and y==0:       #если оба числа нули
            return Natural('0')
        if x==0:        #если первое число ноль
            raise ValueError("the difference must not be negative")
        result=other.MUL_ND_N(digit)        #второе число умножаем на цифру
        if result.COM_NN_D(result):
            raise ValueError("the difference must not be negative")
        return self.SUB_NN_N(result)        #вычитаем числа

    # Вычисление первой цифры деления большего натурального на меньшее, домноженное на 10^k, где k - номер позиции этой цифры (номер считается с нуля)
    def DIV_NN_Dk(self, other, k):
        if other.COM_NN_D(Natural('0'))==0:     #если первое число равно нулю
            raise ValueError("Сan not divide by zero")
        if other.COM_NN_D(self) == 2:       #если делитель больше делимого
            raise ValueError("Cannot divide a larger number by a smaller one")
        divisor = other.MUL_Nk_N(k)              #дописываем нолики в конец
        for i in range(10):
            if divisor.MUL_ND_N(i).COM_NN_D(self) == 2:             #умножаем divisor на i, сравниваем числа
                return i - 1
        if divisor.MUL_NN_N(Natural('10')).COM_NN_D(self) == 1:
            raise ValueError('Incorrect position number')
        return 9

    # Неполное частное от деления первого натурального числа на второе с остатком (делитель отличен от нуля)
    def DIV_NN_N(self, other):
        if other.COM_NN_D(Natural('0')) == 0:           #если делитель равен нулю выкидываем предупреждение
            raise ValueError("Сan not divide by zero")
        if other.COM_NN_D(Natural('1')) == 0: return self           #если делитель равен нулю, то частное равно делимому
        socmp = self.COM_NN_D(other)
        if socmp == 1: return Natural('0')           #если делитель больше делимого, то частное равно 0
        if socmp == 0: return Natural('1')           #если делитель равен делимому, то частное равно 1
        n=len(self.number)          #длина делимого
        m=len(other.number)           #длина делителя
        dl1=Natural('0')            #списки для разделения числа которое мы делим
        dl2 = Natural('0')
        result=Natural('0')
        result.number = []
        dl1.number=self.number[:m]            #отрезаем от делимого(self) часть длиной делителя(m)
        dl2.number=self.number[m:]             #отрезаем оставшуюся часть от делимого после прошлого действия
        el = Natural('0')
        for i in range(0,n-m+1):
            # если ноль ведущий, то удаляем его
            while len(dl1.number) > 1 and dl1.number[0] == 0:
                dl1.number.pop(0)
            # если делитель, больше взятой части делимого, то добавляем в результат ноль
            if dl1.COM_NN_D(other)==1:
                x=0
            else:
                x=dl1.DIV_NN_Dk(other,0)            # определяем частное для текущей части делимого
                el=dl1.SUB_NDN_N(other,x)       # вычитаем произведение делителя на частное из текущей части делимого
                dl1 = el        # обновляем dl1 остатком
            if len(result.number)!=0 or x!=0:       #не записываем незначащие нули
                result.number.append(x)
            if  len(dl2.number)!=0:
                dl1.number.append(dl2.number[0])        # добавляем старший разряд из dl2 к dl1
                dl2.number=dl2.number[1:]       # удаляем этот разряд из dl2
        return result


    # Остаток от деления первого натурального числа на второе натуральное (делитель отличен от нуля)
    def MOD_NN_N(self, other):
        if other.COM_NN_D(Natural('0')) == 0:           #если делитель равен нулю выкидываем предупреждение
            raise ValueError("Сan not divide by zero")
        if other.COM_NN_D(Natural('1')) == 0: return Natural('0')           #если делитель равен единице, то остаток равен 0
        socmp = self.COM_NN_D(other)            #результат сравнения
        if socmp == 1: return self          #если делитель больше делимого, то остаток равен делимому
        if socmp == 0: return Natural('0')           #если делитель равен делимому, то остаток равен 0
        quotient = self.DIV_NN_N(other)         # частное от деления одного на другое
        return self.SUB_NN_N(quotient.MUL_NN_N(other))      #умножаем частное на делитель и вычитаем из делителя

    # НОД натуральных чисел
    def GCF_NN_N(self, other):
        a = Natural(str(self))
        b = Natural(str(other))
        x=self.COM_NN_D(Natural('0'))
        y=other.COM_NN_D(Natural('0'))
        if  x== 0 and y==0:     #если оба числа нули
            return 1
        if x==0:        #если одного из чисел ноль
            return b
        if y==0:
            return a
        if self.COM_NN_D(Natural('1'))==0 or other.COM_NN_D(Natural('1'))==0:   #если либо первое, либо второе единица
            return 1
        if self.COM_NN_D(other) == 2: a,b = b,a
        while a.NZER_N_B() and b.NZER_N_B():    #пока не нули
            a, b = b, a.MOD_NN_N(b)     #находим остатки
        return a

    # НОК натуральных чисел
    def LCM_NN_N(self, other):
        x=self.COM_NN_D(Natural('0'))
        y=other.COM_NN_D(Natural('0'))
        if  x== 0 and y==0: #если оба числа нули
            raise ValueError("there are no LCM for two zeros")
        if  x==0 or y==0:   #если одно из чисел ноль
            raise ValueError("LCM does not exist when one of the numbers is zero")
        if self.COM_NN_D(Natural('1'))==0:      #если одно из чисел единица
            return Natural(str(other))
        if other.COM_NN_D(Natural('1'))==0:
            return Natural(str(self))
        return self.MUL_NN_N(other).DIV_NN_N(self.GCF_NN_N(other))


# Тестики (нужно допилить)
def Natural_tests():
    num1 = Natural("123")
    num2 = Natural("456")
    num3 = Natural("1000")
    num4 = Natural("999")
    num5 = Natural("0")
    num6 = Natural("2000")
    n1 = Natural('23')
    n2 = Natural('0')
    n3=Natural('1')
    def test_COM_NN_D():
        print("Сравнение:")
        print(f"{num1} < {num2}: {num1.COM_NN_D(num2)}")  # 1
        print(f"{num2} > {num1}: {num2.COM_NN_D(num1)}")  # 2
        print(f"{num1} == {num1}: {num1.COM_NN_D(num1)}")  # 0
        print()
    def test_NZER_N_B():
        print("Проверка на ноль:")
        print(f"{num1} ≠ 0: {num1.NZER_N_B()}")       # True
        print(f"{num5} ≠ 0: {num5.NZER_N_B()}")       # False
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
        print(f"{num1} ∙ 2 = {num1.MUL_ND_N(2)}")      # 246
        print(f"{num1} ∙ 9 = {num1.MUL_ND_N(9)}")      # 1107
        print(f"{num1} ∙ 10^3 = {num1.MUL_Nk_N(3)}")  # 123000
        print(f"{num1} ∙ 10^0 = {num1.MUL_Nk_N(0)}")  # 123
        print(f"{num1} ∙ {num3} = {num1.MUL_NN_N(num3)}")   # 123000
        print(f"{num1} ∙ {num2} = {num1.MUL_NN_N(num2)}")   # 56088
        print()
    def test_SUB_NDN_N():
        print("Вычитание с умножением:")
        print(f"{num3} - ({num1} ∙ 2) = {num3.SUB_NDN_N(num1, 2)}")  # 754
        print(f"{num3} - ({num4} ∙ 1) = {num3.SUB_NDN_N(num4, 1)}")  # 1
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
        #print(f"{n1} % {n2} = {n1.MOD_NN_N(n2)}")  # 0
        #print(f"{num5} % {n2} = {num5.MOD_NN_N(n2)}")  # 0
        print(f"{num1} % {num1} = {num1.MOD_NN_N(num1)}")
        print()
    def test_GCF_NN_N():
        print("Наибольший общий делитель (НОД):")
        print(f"НОД({num2}, {num3}) = {num2.GCF_NN_N(num3)}")# 8
        print(f"НОД({n1}, {n2}) = {n1.GCF_NN_N(n2)}")
        print(f"НОД({n2}, {n1}) = {n2.GCF_NN_N(n1)}")
        print(f"НОД({n1}, {n3}) = {n1.GCF_NN_N(n3)}")
        print(f"НОД({n3}, {n1}) = {n3.GCF_NN_N(n1)}")
        #print(f"НОД({num5}, {n2}) = {num5.GCF_NN_N(n2)}")
        print()
    def test_LCM_NN_N():
        print("Наименьшее общее кратное (НОК):")
        print(f"НОК({num2}, {num3}) = {num2.LCM_NN_N(num3)}")   # 57000
        #print(f"НОК({num5}, {n2}) = {num5.LCM_NN_N(n2)}") 0 и 0
        #print(f"НОК({n1}, {n2}) = {n1.LCM_NN_N(n2)}")     23 и 0
        print(f"НОК({n3}, {n1}) = {n3.LCM_NN_N(n1)}")      #23
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
    #a=Natural('1000')
    #b = Natural('123')
    #c=a.DIV_NN_N(b)
    #print(c)


