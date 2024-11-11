import tkinter as tk
from tkinter import messagebox
from modules.Natural import *
from modules.Integer import *
from modules.Rational import *
from modules.Polynomial import *
from modules.additionally import *
import argparse


class PolynomialApp:
    def __init__(self, root, theme='dark'):
        # Определение цветов в зависимости от темы
        if theme == 'light':
            self.bg_color = "#FFFFFF"  # Цвет фона
            self.window_color = "#EAEAEA"  # Цвет окон
            self.text_color = "#2e2e2e"  # Цвет текста
            self.backlight = "#2e2e2e"  # Цвет подсветки текста
        else:  # Темная тема по умолчанию
            self.bg_color = "#24252b"  # Цвет фона
            self.window_color = "#3e404d"  # Цвет окон
            self.text_color = "#F5F5F5"  # Цвет текста
            self.backlight = "#F5F5F5"  # Цвет подсветки текста

        self.hover_color = "#78aaff"  # Цвет при наведении
        self.button_color = "#6495ED"  # Цвет для кнопки
        self.root = root
        self.root.title("Polynomial Operations")
        self.root.geometry("360x420")
        self.root.configure(bg=self.bg_color)
        self.root.attributes('-alpha', 1)

        self.method_var = tk.StringVar(value="Сложение многочленов")

        # Заголовок
        title_label = tk.Label(root, text="Операции с многочленами", bg=self.bg_color, fg=self.text_color, font=("Arial", 16))
        title_label.pack(pady=12)

        # Выбор метода
        methods = [
            "Сложение многочленов",
            "Вычитание многочленов",
            "Умножение на дробь",
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

        tk.Label(method_frame, text="Операция:  ", bg=self.bg_color, fg=self.text_color, font=("Arial", 10)).pack(side=tk.LEFT)

        self.method_menu = tk.OptionMenu(method_frame, self.method_var, *methods, command=self.on_option_change)
        self.method_menu.config(bg=self.bg_color, fg=self.text_color, highlightbackground=self.button_color,
                                relief=tk.FLAT, activebackground=self.window_color, activeforeground=self.text_color,
                                highlightthickness=2, font=("Arial", 10))
        self.method_menu.pack(side=tk.LEFT)

        # Ввод первого числа
        self.first_polynomial_label = tk.Label(root, text="✔ Введите первый многочлен:", bg=self.bg_color, fg=self.backlight, font=("Arial", 10))
        self.first_polynomial_label.pack(pady=5)
        self.first_polynomial_entry = tk.Entry(root, bg=self.window_color, fg=self.text_color, width=26, insertbackground='black' if theme == 'light' else 'white', font=("Arial", 14))
        self.first_polynomial_entry.pack(pady=5)

        # Ввод второго числа
        self.second_polynomial_label = tk.Label(root, text="✔ Введите второй многочлен:", bg=self.bg_color, fg=self.backlight, font=("Arial", 10))
        self.second_polynomial_label.pack(pady=5)
        self.second_polynomial_entry = tk.Entry(root, bg=self.window_color, fg=self.text_color, width=26, insertbackground='black' if theme == 'light' else 'white', font=("Arial", 14))
        self.second_polynomial_entry.pack(pady=5)

        # Ввод цифры
        self.digit_label = tk.Label(root, text="Введите число:", bg=self.bg_color, fg=self.text_color, font=("Arial", 10))
        self.digit_label.pack(pady=5)
        self.digit_entry = tk.Entry(root, bg=self.window_color, fg=self.text_color, insertbackground='black' if theme == 'light' else 'white', font=("Arial", 14))
        self.digit_entry.pack(pady=5)

        # Метка для результата
        self.result_label = tk.Label(root, text="", bg=self.bg_color, fg=self.text_color, font=("Arial", 14))
        self.result_label.pack(pady=10)

        # Кнопка для выполнения операции
        self.calculate_button = tk.Button(root, text="Выполнить", command=self.calculate, bg=self.button_color, fg="white", font=("Arial", 14), height=1, width=15, relief=tk.FLAT)
        self.calculate_button.place(relx=0.5, y=380, anchor=tk.CENTER)
        self.calculate_button.bind("<Enter>", lambda e: self.calculate_button.config(bg=self.hover_color))
        self.calculate_button.bind("<Leave>", lambda e: self.calculate_button.config(bg=self.button_color))
        methods = [
            "Сложение многочленов",
            "Вычитание многочленов",
            "Умножение на дробь",
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
    def on_option_change(self, value):
        method_name = self.method_var.get()
        self.second_polynomial_label.config(fg=self.text_color, text="Введите второй многочлен:")
        self.digit_label.config(fg=self.text_color, text="Введите число:")
        if method_name in ["Сложение многочленов",
                           "Вычитание многочленов",
                           "Умножение многочленов",
                           "Частное от деления",
                           "Остаток от деления",
                           "НОД"]:
            self.second_polynomial_label.config(fg=self.backlight, text="✔ Введите второй многочлен:")
        elif method_name in ["Умножение на дробь",
                             "Умножение на xⁿ"]:
            self.digit_label.config(fg=self.backlight, text="✔ Введите число:")

    def calculate(self):
        method_name = self.method_var.get()
        first_polynomial_str = self.first_polynomial_entry.get()


        try:
            first_polynomial = get_Polynomial(first_polynomial_str)
        except ValueError:
            if first_polynomial_str == '':
                messagebox.showerror("Ошибка", f"Первый многочлен не введен.")
            else:
                messagebox.showerror("Ошибка", f"Неверный ввод первого многочлена.")
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
                if second_polynomial_str == '':
                    messagebox.showerror("Ошибка", f"Второй многочлен не введен.")
                else:
                    messagebox.showerror("Ошибка", f"Неверный ввод второго многочлена.")
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
            if method_name == "Умножение на дробь":
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
                result = first_polynomial.NMP_P_P()
                self.result_label.config(text=f"Результат: {result}")


def create_PolynomialApp(root, theme):
    new_root = tk.Toplevel(root)
    app = PolynomialApp(new_root, theme=theme)
    return app


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Polynomial Operations App')
    parser.add_argument('--theme', type=str, choices=['light', 'dark'], default='dark',
                        help='Choose the theme of the application')

    args = parser.parse_args()

    root = tk.Tk()
    app = PolynomialApp(root, theme=args.theme)  # Передача темы из аргументов командной строки
    root.mainloop()
