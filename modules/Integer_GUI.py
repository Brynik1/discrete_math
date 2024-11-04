import tkinter as tk
from tkinter import messagebox
from Natural import *
from Integer import *
from additionally import *


class IntegerApp:
    def __init__(self, root):
        # Определение цветов
        self.bg_color = "#1e1f22"  # Цвет фона
        self.window_color = "#2b2d30"  # Цвет окон
        self.text_color = "white"  # Цвет текста
        self.hover_color = "#3c3f42"  # Цвет при наведении

        self.root = root
        self.root.title("Integer Number Operations")
        self.root.geometry("374x420")
        self.root.configure(bg=self.bg_color)
        self.root.attributes('-alpha', 0.98)

        self.method_var = tk.StringVar(value="Сложение двух чисел")

        # Заголовок
        title_label = tk.Label(root, text="Операции с целыми числами", bg=self.bg_color, fg=self.text_color, font=("Arial", 16))
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

        tk.Label(method_frame, text="Выберите метод:", bg=self.bg_color, fg=self.text_color, font=("Arial", 10)).pack(side=tk.LEFT)

        self.method_menu = tk.OptionMenu(method_frame, self.method_var, *methods)
        self.method_menu.config(bg=self.window_color, fg=self.text_color, highlightbackground=self.window_color)

        # Настройка событий для изменения цвета фона
        self.method_menu.bind("<Enter>", lambda e: self.method_menu.config(bg=self.hover_color))
        self.method_menu.bind("<Leave>", lambda e: self.method_menu.config(bg=self.window_color))

        self.method_menu.pack(side=tk.LEFT)

        # Ввод первого числа
        tk.Label(root, text="Введите первое число:", bg=self.bg_color, fg=self.text_color, font=("Arial", 10)).pack(pady=5)
        self.first_number_entry = tk.Entry(root, bg=self.window_color, fg=self.text_color, insertbackground='white',
                                           font=("Arial", 14))
        self.first_number_entry.pack(pady=5)

        # Ввод второго числа
        tk.Label(root, text="Введите второе число (если необходимо):", bg=self.bg_color, fg=self.text_color, font=("Arial", 10)).pack(pady=5)
        self.second_number_entry = tk.Entry(root, bg=self.window_color, fg=self.text_color, insertbackground='white', font=("Arial", 14))
        self.second_number_entry.pack(pady=5)

        # Ввод цифры
        tk.Label(root, text="Введите цифру (для методов с цифрой):", bg=self.bg_color, fg=self.text_color, font=("Arial", 10)).pack(pady=5)
        self.digit_entry = tk.Entry(root, bg=self.window_color, fg=self.text_color, insertbackground='white',
                                    font=("Arial", 14))
        self.digit_entry.pack(pady=5)

        # Метка для результата
        self.result_label = tk.Label(root, text="", bg=self.bg_color, fg=self.text_color, font=("Arial", 14))
        self.result_label.pack(pady=10)

        # Кнопка для выполнения операции
        self.calculate_button = tk.Button(root, text="Выполнить", command=self.calculate, bg="#4CAF50",
                                          fg=self.text_color, font=("Arial", 14), height=1, width=15)
        self.calculate_button.pack(pady=10)
        self.calculate_button.bind("<Enter>", lambda e: self.calculate_button.config(bg="#61e867"))
        self.calculate_button.bind("<Leave>", lambda e: self.calculate_button.config(bg="#4CAF50"))

    def calculate(self):
        method_name = self.method_var.get()
        first_number_str = self.first_number_entry.get()

        if not is_Integer(first_number_str):
            messagebox.showerror("Ошибка", "Первое число должно быть целым.")
            return

        first_number = get_Integer(first_number_str)
        if method_name in ["Сложение двух чисел",
                        "Вычитание двух чисел",
                        "Умножение двух чисел",
                        "Деление целочисленное",
                        "Деление с остатком"]:
            second_number_str = self.second_number_entry.get()
            if not is_Integer(second_number_str):
                messagebox.showerror("Ошибка", "Второе число должно быть целым.")
                return

            second_number = get_Integer(second_number_str)

            if method_name == "Сложение двух чисел":
                result = first_number.ADD_ZZ_Z(second_number)
                self.result_label.config(text=f"{first_number} + {second_number} = {result}")

            elif method_name == "Вычитание двух чисел":
                try:
                    result = first_number.SUB_ZZ_Z(second_number)
                    self.result_label.config(text=f"{first_number} - {second_number} = {result}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", str(e))
                    return

            elif method_name == "Умножение двух чисел":
                result = first_number.MUL_ZZ_Z(second_number)
                self.result_label.config(text=f"{first_number} ∙ {second_number} = {result}")

            elif method_name == "Деление целочисленное":
                result = first_number.DIV_ZZ_Z(second_number)
                self.result_label.config(text=f"{first_number} div {second_number} = {result}")

            elif method_name == "Деление с остатком":
                result = first_number.MOD_ZZ_Z(second_number)
                self.result_label.config(text=f"{first_number} mod {second_number} = {result}")


        #"Модуль числа",
        #"Определение знака",
        #"Умножение на -1",
        #"Натуральное -> целое",
        #"Целое -> натуральное",

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
                self.result_label.config(text=f"Результат: {result}")


            elif method_name == "Натуральное -> целое":
                if not is_Natural(first_number_str):
                    messagebox.showerror("Ошибка", "Первое число должно быть натуральным.")
                    return
                natural = get_Natural(first_number_str)
                result = Integer.TRANS_N_Z(natural)
                self.result_label.config(text=f"Результат: {result}")

            elif method_name == "Целое -> натуральное":
                result = Integer.TRANS_N_Z(first_number)
                self.result_label.config(text=f"Результат: {result}")



if __name__ == "__main__":
    root = tk.Tk()
    app = IntegerApp(root)
    root.mainloop()
