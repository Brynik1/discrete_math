import tkinter as tk
from tkinter import messagebox
from Natural import *
from Integer import *
from Rational import *
from Polynomial import *
from additionally import *


class PolynomialApp:
    def __init__(self, root):
        # Определение цветов
        self.bg_color = "#1e1f22"  # Цвет фона
        self.window_color = "#2b2d30"  # Цвет окон
        self.text_color = "white"  # Цвет текста
        self.hover_color = "#3c3f42"  # Цвет при наведении

        self.root = root
        self.root.title("Polynomial Operations")
        self.root.geometry("374x420")
        self.root.configure(bg=self.bg_color)
        self.root.attributes('-alpha', 0.98)

        self.method_var = tk.StringVar(value="Сложение многочленов")

        # Заголовок
        title_label = tk.Label(root, text="Операции с многочленами", bg=self.bg_color, fg=self.text_color, font=("Arial", 16))
        title_label.pack(pady=10)

        # Выбор метода
        methods = [
            "Сложение многочленов",
            "Вычитание многочленов",
            "Умножение на рациональное число",
            "Умножение на xⁿ",
            "Старший коэффициент",
            "НОК знаменателей и НОД числителей",
            "Умножение многочленов",
            "Частное от деления",
            "Остаток от деления",
            "НОД",
            "Производная",
            "Кратные корни в простые"
        ]

        method_frame = tk.Frame(root, bg=self.bg_color)
        method_frame.pack(pady=10)

        tk.Label(method_frame, text="Выберите метод:", bg=self.bg_color, fg=self.text_color, font=("Arial", 10)).pack(side=tk.LEFT)

        self.method_menu = tk.OptionMenu(method_frame, self.method_var, *methods)
        self.method_menu.config(bg=self.window_color, fg=self.text_color, highlightbackground=self.window_color)

        # Настройка событий для изменения цвета фона
        self.method_menu.bind("<Enter>", lambda e: self.method_menu.config(bg=self.hover_color))
        self.method_menu.bind("<Leave>", lambda e: self.method_menu.config(bg=self.window_color))
        self.method_menu.pack(side=tk.LEFT)

        # Ввод первого числа
        tk.Label(root, text="Введите первый многочлен:", bg=self.bg_color, fg=self.text_color, font=("Arial", 10)).pack(pady=5)
        self.first_polynomial_entry = tk.Entry(root, bg=self.window_color, fg=self.text_color, insertbackground='white', font=("Arial", 14))
        self.first_polynomial_entry.pack(pady=5)

        # Ввод второго числа
        tk.Label(root, text="Введите второй многочлен (если необходимо):", bg=self.bg_color, fg=self.text_color, font=("Arial", 10)).pack(pady=5)
        self.second_polynomial_entry = tk.Entry(root, bg=self.window_color, fg=self.text_color, insertbackground='white', font=("Arial", 14))
        self.second_polynomial_entry.pack(pady=5)

        # Ввод цифры
        tk.Label(root, text="Введите число (для методов с числом):", bg=self.bg_color, fg=self.text_color, font=("Arial", 10)).pack(pady=5)
        self.digit_entry = tk.Entry(root, bg=self.window_color, fg=self.text_color, insertbackground='white', font=("Arial", 14))
        self.digit_entry.pack(pady=5)

        # Метка для результата
        self.result_label = tk.Label(root, text="", bg=self.bg_color, fg=self.text_color, font=("Arial", 14))
        self.result_label.pack(pady=10)

        # Кнопка для выполнения операции
        self.calculate_button = tk.Button(root, text="Выполнить", command=self.calculate, bg="#4CAF50", fg=self.text_color, font=("Arial", 14), height=1, width=15)
        self.calculate_button.pack(pady=10)
        self.calculate_button.bind("<Enter>", lambda e: self.calculate_button.config(bg="#61e867"))
        self.calculate_button.bind("<Leave>", lambda e: self.calculate_button.config(bg="#4CAF50"))


    def calculate(self):
        method_name = self.method_var.get()
        first_polynomial_str = self.first_polynomial_entry.get()


        try:
            first_polynomial = get_Polynomial(first_polynomial_str)
        except ValueError:
            messagebox.showerror("Ошибка", "Первое число должно быть многочленом.")
            return

        if method_name in ["Сложение многочленов",
                           "Вычитание многочленов",
                           "Умножение многочленов",
                           "Частное от деления",
                           "Остаток от деления",
                           "НОД",]:

            second_polynomial_str = self.second_polynomial_entry.get()
            try:
                second_polynomial = get_Polynomial(second_polynomial_str)
            except ValueError:
                messagebox.showerror("Ошибка", "Второе число должно быть многочленом.")
                return

            if method_name == "Сложение многочленов":
                result = first_polynomial.ADD_PP_P(second_polynomial)
                self.result_label.config(text=f"Результат: {result}")

            elif method_name == "Вычитание многочленов":
                result = first_polynomial.SUB_PP_P(second_polynomial)
                self.result_label.config(text=f"Результат: {result}")

            elif method_name == "Умножение многочленов":
                result = first_polynomial.MUL_PP_P(second_polynomial)
                self.result_label.config(text=f"Результат: {result}")

            elif method_name == "Частное от деления":
                result = first_polynomial.DIV_PP_P(second_polynomial)
                self.result_label.config(text=f"Результат: {result}")

            elif method_name == "Остаток от деления":
                result = first_polynomial.MOD_PP_P(second_polynomial)
                self.result_label.config(text=f"Результат: {result}")

            elif method_name == "НОД":
                result = first_polynomial.GCF_PP_P(second_polynomial)
                self.result_label.config(text=f"НОД: {result}")


        else:
            if method_name == "Умножение на рациональное число":
                number_str = self.digit_entry.get()
                if not is_Rational(number_str):
                    messagebox.showerror("Ошибка", "Первое число должно быть рациональным.")
                    return
                number = get_Rational(number_str)
                result = first_polynomial.MUL_PQ_P(number)
                self.result_label.config(text=f"Результат: {result}")

            elif method_name == "Умножение на xⁿ":
                k_str = self.digit_entry.get()
                if not is_Natural(k_str):
                    messagebox.showerror("Ошибка", "k должно быть неотрицательным целым числом.")
                    return
                k = int(k_str)
                result = first_polynomial.MUL_Pxk_P(k)
                self.result_label.config(text=f"Результат: {result}")

            elif method_name == "Старший коэффициент":
                result = first_polynomial.LED_P_Q()
                self.result_label.config(text=f"deg = {result}")

            elif method_name == "НОК знаменателей и НОД числителей":
                result = first_polynomial.FAC_P_Q()
                self.result_label.config(text=f"НОД/НОК = {result}")

            elif method_name == "Производная":
                result = first_polynomial.DER_P_P()
                self.result_label.config(text=f"Производная: {result}")

            elif method_name == "Кратные корни в простые":
                self.result_label.config(text=f"Answer")
                #result = first_polynomial.NMP_P_P()
                #self.result_label.config(text=f"Результат: {result}")


if __name__ == "__main__":
    root = tk.Tk()
    app = PolynomialApp(root)
    root.mainloop()
