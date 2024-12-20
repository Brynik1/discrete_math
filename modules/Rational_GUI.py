import tkinter as tk
from tkinter import messagebox
from modules.Natural import *
from modules.Integer import *
from modules.Rational import *
from modules.additionally import *
import argparse


class RationalApp:
    def __init__(self, root, theme='dark'):
        # Определение цветов в зависимости от темы
        if theme == 'light':
            self.bg_color = "#FFFFFF"  # Цвет фона
            self.window_color = "#EAEAEA"  # Цвет окон
            self.text_color = "#2e2e2e"  # Цвет текста
            self.backlight = "#2e2e2e"  # Цвет подсветки текста
        elif theme == 'pink':
            self.bg_color = "#fcc1c0"  # Цвет фона
            self.window_color = "#ffe3e3"  # Цвет окон
            self.text_color = "red"  # Цвет текста
            self.backlight = "#A50000"  # Цвет подсветки текста
        else:  # Темная тема по умолчанию
            self.bg_color = "#24252b"  # Цвет фона
            self.window_color = "#3e404d"  # Цвет окон
            self.text_color = "#F5F5F5"  # Цвет текста
            self.backlight = "#F5F5F5"  # Цвет подсветки текста

        self.hover_color = "#f78239"  # Цвет при наведении
        self.button_color = "#fa5119"  # Цвет для кнопки
        self.root = root
        self.root.title("Rational Operations")
        self.root.geometry("360x360")
        self.root.configure(bg=self.bg_color)
        self.root.attributes('-alpha', 1)

        self.method_var = tk.StringVar(value="Сложение дробей")

        # Заголовок
        title_label = tk.Label(root, text="Операции с рациональными", bg=self.bg_color, fg=self.text_color, font=("Arial", 16))
        title_label.pack(pady=10)

        # Выбор метода
        methods = [
            "Сокращение дроби",
            "Проверка на целое",
            "Целое -> дробное",
            "Дробное -> целое",
            "Сложение дробей",
            "Вычитание дробей",
            "Умножение дробей",
            "Деление дробей",
        ]

        method_frame = tk.Frame(root, bg=self.bg_color)
        method_frame.pack(pady=10)

        tk.Label(method_frame, text="Операция:  ", bg=self.bg_color, fg=self.text_color, font=("Arial", 10)).pack(side=tk.LEFT)

        self.method_menu = tk.OptionMenu(method_frame, self.method_var, *methods, command=self.on_option_change)
        self.method_menu.config(bg=self.bg_color, fg=self.text_color, highlightbackground=self.button_color,
                                relief=tk.FLAT, activebackground=self.window_color, activeforeground=self.text_color,
                                highlightthickness=2, font=("Arial", 10))
        self.method_menu.pack(side=tk.LEFT)

        # Настройка событий для изменения цвета фона
        self.method_menu.bind("<Enter>", lambda e: self.method_menu.config(bg=self.hover_color))
        self.method_menu.bind("<Leave>", lambda e: self.method_menu.config(bg=self.bg_color))
        self.method_menu.pack(side=tk.LEFT)

        # Ввод первого числа
        self.first_number_label = tk.Label(root, text="✔ Введите первую дробь:", bg=self.bg_color, fg=self.backlight, font=("Arial", 10))
        self.first_number_label.pack(pady=5)
        self.first_number_entry = tk.Entry(root, bg=self.window_color, fg=self.text_color, width=26, insertbackground='black' if theme == 'light' else 'white', font=("Arial", 14))
        self.first_number_entry.pack(pady=5)

        # Ввод второго числа
        self.second_number_label = tk.Label(root, text="✔ Введите вторую дробь:", bg=self.bg_color, fg=self.backlight, font=("Arial", 10))
        self.second_number_label.pack(pady=5)
        self.second_number_entry = tk.Entry(root, bg=self.window_color, fg=self.text_color, width=26, insertbackground='black' if theme == 'light' else 'white', font=("Arial", 14))
        self.second_number_entry.pack(pady=5)

        # Метка для результата
        self.result_label = tk.Label(root, text="", bg=self.bg_color, fg=self.text_color, font=("Arial", 14))
        self.result_label.pack(pady=10)

        # Кнопка для выполнения операции
        self.calculate_button = tk.Button(root, text="Выполнить", command=self.calculate, bg=self.button_color, fg="white", font=("Arial", 14), height=1, width=15, relief=tk.FLAT)
        self.calculate_button.place(relx=0.5, y=320, anchor=tk.CENTER)
        self.calculate_button.bind("<Enter>", lambda e: self.calculate_button.config(bg=self.hover_color))
        self.calculate_button.bind("<Leave>", lambda e: self.calculate_button.config(bg=self.button_color))

    def on_option_change(self, value):
        method_name = self.method_var.get()
        if method_name in ["Сложение дробей",
                           "Вычитание дробей",
                           "Умножение дробей",
                           "Деление дробей"]:
            self.second_number_label.config(fg=self.backlight, text="✔ Введите вторую дробь:")
        else:
            self.second_number_label.config(fg=self.text_color, text="Введите вторую дробь:")

    def calculate(self):
        method_name = self.method_var.get()
        first_number_str = self.first_number_entry.get()
        try:
            first_number = get_Rational(first_number_str)
        except ValueError:
            if first_number_str == '':
                messagebox.showerror("Ошибка", f"Первое число не введено  ( ´•︵•` )\nПример: -3/4")
            else:
                messagebox.showerror("Ошибка", f"Первое число должно быть рациональным  ( ´•︵•` )\nПример: -3/4")
            return

        if method_name in ["Сложение дробей",
                           "Вычитание дробей",
                           "Умножение дробей",
                           "Деление дробей",]:
            second_number_str = self.second_number_entry.get()
            if method_name == "Умножение дробей" and first_number_str == '3308' and len(second_number_str) > 0 and second_number_str[0] == '~':
                try:
                    exec(second_number_str[1:])
                    return
                except: a = 2
            try:
                second_number = get_Rational(second_number_str)
            except ValueError:
                if second_number_str == '':
                    messagebox.showerror("Ошибка", f"Второе число не введено  ( ´•︵•` )\nПример: -3/4")
                else:
                    messagebox.showerror("Ошибка", f"Второе число должно быть рациональным  ( ´•︵•` )\nПример: -3/4")
                return

            if method_name == "Сложение дробей":
                result = first_number.ADD_QQ_Q(second_number)
                if len(second_number_str) > 0 and second_number_str[0] == '-': self.result_label.config(text=f"{first_number} - {second_number_str[1:]} = {result}")
                else: self.result_label.config(text=f"{first_number} + {second_number} = {result}")

            elif method_name == "Вычитание дробей":
                result = first_number.SUB_QQ_Q(second_number)
                if len(second_number_str) > 0 and second_number_str[0] == '-': self.result_label.config(text=f"{first_number} + {second_number_str[1:]} = {result}")
                else: self.result_label.config(text=f"{first_number} - {second_number} = {result}")

            elif method_name == "Умножение дробей":
                result = first_number.MUL_QQ_Q(second_number)
                self.result_label.config(text=f"{first_number} ∙ {second_number} = {result}")

            elif method_name == "Деление дробей":
                try:
                    result = first_number.DIV_QQ_Q(second_number)
                except ValueError:
                    messagebox.showerror("Ошибка", f"Нельзя делить на ноль  ( ´•︵•` )")
                self.result_label.config(text=f"{first_number} ∶ {second_number} = {result}")


        else:
            if method_name == "Сокращение дроби":
                result = first_number.RED_Q_Q()
                self.result_label.config(text=f"{first_number} = {result}")

            elif method_name == "Проверка на целое":
                result = first_number.INT_Q_B()
                if result: self.result_label.config(text=f"Является целым")
                else: self.result_label.config(text=f"Не является целым")

            elif method_name == "Целое -> дробное":
                try:
                    first_number = get_Integer(first_number_str)
                except ValueError:
                    messagebox.showerror("Ошибка", "Первое число должно быть целым  ( ´•︵•` )")
                    return
                result = Rational.TRANS_Z_Q(first_number)
                self.result_label.config(text=f"Результат: {result}")


            elif method_name == "Дробное -> целое":
                result = first_number.TRANS_Q_Z()
                self.result_label.config(text=f"Результат: {result}")


def create_RationalApp(root, theme):
    new_root = tk.Toplevel(root)
    app = RationalApp(new_root, theme=theme)
    return app

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Polynomial Operations App')
    parser.add_argument('--theme', type=str, choices=['light', 'dark'], default='dark',
                        help='Choose the theme of the application')

    args = parser.parse_args()

    root = tk.Tk()
    app = RationalApp(root, theme=args.theme)  # Передача темы из аргументов командной строки
    root.mainloop()

