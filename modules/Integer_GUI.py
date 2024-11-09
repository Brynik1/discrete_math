import tkinter as tk
from tkinter import messagebox
from Natural import *
from Integer import *
from additionally import *
import argparse


class IntegerApp:
    def __init__(self, root, theme='dark'):
        # Определение цветов в зависимости от темы
        if theme == 'light':
            self.bg_color = "#FFFFFF"  # Цвет фона
            self.window_color = "#EAEAEA"  # Цвет окон
            self.text_color = "#2e2e2e"  # Цвет текста
            self.hover_color = "#61e867"  # Цвет при наведении
            self.button_color = "#5ebf62"  # Цвет для кнопки
        else:  # Темная тема по умолчанию
            self.bg_color = "#232323"  # Цвет фона
            self.window_color = "#3A3A3A"  # Цвет окон
            self.text_color = "#F5F5F5"  # Цвет текста
            self.hover_color = "#61e867"  # Цвет при наведении
            self.button_color = "#4CAF50"  # Цвет для кнопки

        self.root = root
        self.root.title("Integer Operations")
        self.root.geometry("360x360")
        self.root.configure(bg=self.bg_color)
        self.root.attributes('-alpha', 1)

        self.method_var = tk.StringVar(value="Сложение двух чисел")

        # Заголовок
        title_label = tk.Label(root, text="Операции с целыми", bg=self.bg_color, fg=self.text_color, font=("Arial", 16))
        title_label.pack(pady=10)

        # Выбор метода
        methods = [
            "Модуль числа",
            "Определение знака",
            "Умножение на -1",
            "Натуральное -> целое",
            "Целое -> натуральное",
            "Сложение двух чисел",
            "Вычитание двух чисел",
            "Умножение двух чисел",
            "Деление целочисленное",
            "Деление с остатком"
        ]

        method_frame = tk.Frame(root, bg=self.bg_color)
        method_frame.pack(pady=10)

        tk.Label(method_frame, text="Операция:  ", bg=self.bg_color, fg=self.text_color, font=("Arial", 10)).pack(side=tk.LEFT)

        self.method_menu = tk.OptionMenu(method_frame, self.method_var, *methods)
        self.method_menu.config(bg=self.bg_color, fg=self.text_color, highlightbackground=self.button_color,
                                relief=tk.FLAT, activebackground=self.window_color, activeforeground=self.text_color,
                                highlightthickness=2, font=("Arial", 10))
        self.method_menu.pack(side=tk.LEFT)

        # Настройка событий для изменения цвета фона
        self.method_menu.bind("<Enter>", lambda e: self.method_menu.config(bg=self.hover_color))
        self.method_menu.bind("<Leave>", lambda e: self.method_menu.config(bg=self.bg_color))
        self.method_menu.pack(side=tk.LEFT)

        # Ввод первого числа
        tk.Label(root, text="Введите первое число:", bg=self.bg_color, fg=self.text_color, font=("Arial", 10)).pack(pady=5)
        self.first_number_entry = tk.Entry(root, bg=self.window_color, fg=self.text_color, width=26, insertbackground='black' if theme == 'light' else 'white', font=("Arial", 14))
        self.first_number_entry.pack(pady=5)

        # Ввод второго числа
        tk.Label(root, text="Введите второе число (если необходимо):", bg=self.bg_color, fg=self.text_color, font=("Arial", 10)).pack(pady=5)
        self.second_number_entry = tk.Entry(root, bg=self.window_color, fg=self.text_color, width=26, insertbackground='black' if theme == 'light' else 'white', font=("Arial", 14))
        self.second_number_entry.pack(pady=5)

        # Метка для результата
        self.result_label = tk.Label(root, text="", bg=self.bg_color, fg=self.text_color, font=("Arial", 14))
        self.result_label.pack(pady=10)

        # Кнопка для выполнения операции
        self.calculate_button = tk.Button(root, text="Выполнить", command=self.calculate, bg=self.button_color, fg="white", font=("Arial", 14), height=1, width=15, relief=tk.FLAT)
        self.calculate_button.pack(pady=10)
        self.calculate_button.bind("<Enter>", lambda e: self.calculate_button.config(bg=self.hover_color))
        self.calculate_button.bind("<Leave>", lambda e: self.calculate_button.config(bg=self.button_color))

    def calculate(self):
        method_name = self.method_var.get()
        first_number_str = self.first_number_entry.get()

        try:
            first_number = get_Integer(first_number_str)
        except ValueError:
            if first_number_str == '':
                messagebox.showerror("Ошибка", f"Первое число не введено.")
            else:
                messagebox.showerror("Ошибка", f"Первое число должно быть целым.")
            return

        if method_name in ["Сложение двух чисел",
                           "Вычитание двух чисел",
                           "Умножение двух чисел",
                           "Деление целочисленное",
                           "Деление с остатком"]:

            second_number_str = self.second_number_entry.get()

            try:
                second_number = get_Integer(second_number_str)
            except ValueError:
                if second_number_str == '':
                    messagebox.showerror("Ошибка", f"Второе число не введено.")
                else:
                    messagebox.showerror("Ошибка", f"Второе число должно быть целым.")
                return


            if method_name == "Сложение двух чисел":
                result = first_number.ADD_ZZ_Z(second_number)
                if len(second_number_str) > 0 and second_number_str[0] == '-': self.result_label.config(text=f"{first_number} - {second_number_str[1:]} = {result}")
                else: self.result_label.config(text=f"{first_number} + {second_number} = {result}")

            elif method_name == "Вычитание двух чисел":
                result = first_number.SUB_ZZ_Z(second_number)
                if len(second_number_str) > 0 and second_number_str[0] == '-': self.result_label.config(text=f"{first_number} + {second_number_str[1:]} = {result}")
                else: self.result_label.config(text=f"{first_number} - {second_number} = {result}")

            elif method_name == "Умножение двух чисел":
                result = first_number.MUL_ZZ_Z(second_number)
                self.result_label.config(text=f"{first_number} ∙ {second_number} = {result}")

            elif method_name == "Деление целочисленное":
                result = first_number.DIV_ZZ_Z(second_number)
                self.result_label.config(text=f"{first_number} div {second_number} = {result}")

            elif method_name == "Деление с остатком":
                result = first_number.MOD_ZZ_Z(second_number)
                self.result_label.config(text=f"{first_number} mod {second_number} = {result}")


        else:
            if method_name == "Модуль числа":
                result = first_number.ABS_Z_N()
                self.result_label.config(text=f"Результат: {result}")

            elif method_name == "Определение знака":
                result = first_number.POZ_Z_D()
                if result == 2: res = '>'
                elif result == 1: res = '<'
                else: res = '='
                self.result_label.config(text=f"{first_number} {res} 0")

            elif method_name == "Умножение на -1":
                result = first_number.MUL_ZM_Z()
                self.result_label.config(text=f"-1 ∙ {first_number} = {result}")

            elif method_name == "Натуральное -> целое":
                try:
                    natural = get_Natural(first_number_str)
                except ValueError:
                    messagebox.showerror("Ошибка", "Первое число должно быть натуральным.")
                    return
                result = Integer.TRANS_N_Z(natural)
                self.result_label.config(text=f"Результат: {result}")

            elif method_name == "Целое -> натуральное":
                if first_number.POZ_Z_D() == 1:
                    messagebox.showerror("Ошибка", "Первое число должно быть неотрицательным.")
                    return
                result = Integer.TRANS_Z_N(first_number)
                self.result_label.config(text=f"Результат: {result}")



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Polynomial Operations App')
    parser.add_argument('--theme', type=str, choices=['light', 'dark'], default='dark',
                        help='Choose the theme of the application')

    args = parser.parse_args()

    root = tk.Tk()
    app = IntegerApp(root, theme=args.theme)  # Передача темы из аргументов командной строки
    root.mainloop()

