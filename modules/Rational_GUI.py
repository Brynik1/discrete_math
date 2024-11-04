import tkinter as tk
from tkinter import messagebox
from Natural import *
from Integer import *
from Rational import *
from additionally import *


class RationalApp:
    def __init__(self, root):
        # Определение цветов
        self.bg_color = "#1e1f22"  # Цвет фона
        self.window_color = "#2b2d30"  # Цвет окон
        self.text_color = "white"  # Цвет текста
        self.hover_color = "#3c3f42"  # Цвет при наведении

        self.root = root
        self.root.title("Rational Number Operations")
        self.root.geometry("374x350")
        self.root.configure(bg=self.bg_color)
        self.root.attributes('-alpha', 0.98)

        self.method_var = tk.StringVar(value="Сложение дробей")

        # Заголовок
        title_label = tk.Label(root, text="Операции с рациональными числами", bg=self.bg_color, fg=self.text_color, font=("Arial", 16))
        title_label.pack(pady=10)

        # Выбор метода
        methods = [
            "Сокращение дроби",
            "Проверка сокращенного на целое",
            "Целое -> дробное",
            "Дробное -> целое",
            "Сложение дробей",
            "Вычитание дробей",
            "Умножение дробей",
            "Деление дробей",
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
        tk.Label(root, text="Введите первую дробь:", bg=self.bg_color, fg=self.text_color, font=("Arial", 10)).pack(pady=5)
        self.first_number_entry = tk.Entry(root, bg=self.window_color, fg=self.text_color, insertbackground='white', font=("Arial", 14))
        self.first_number_entry.pack(pady=5)

        # Ввод второго числа
        tk.Label(root, text="Введите вторую дробь (если необходимо):", bg=self.bg_color, fg=self.text_color, font=("Arial", 10)).pack(pady=5)
        self.second_number_entry = tk.Entry(root, bg=self.window_color, fg=self.text_color, insertbackground='white', font=("Arial", 14))
        self.second_number_entry.pack(pady=5)

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
        first_number_str = self.first_number_entry.get()
        try:
            first_number = get_Rational(first_number_str)
        except ValueError:
            messagebox.showerror("Ошибка", "Первое число должно быть рациональным.")
            return

        if method_name in ["Сложение дробей",
                           "Вычитание дробей",
                           "Умножение дробей",
                           "Деление дробей",]:

            second_number_str = self.second_number_entry.get()
            try:
                second_number = get_Rational(second_number_str)
            except ValueError:
                messagebox.showerror("Ошибка", "Второе число должно быть рациональным.")
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
                result = first_number.DIV_QQ_Q(second_number)
                self.result_label.config(text=f"{first_number} ∶ {second_number} = {result}")


        else:
            if method_name == "Сокращение дроби":
                result = first_number.RED_Q_Q()
                self.result_label.config(text=f"{first_number} = {result}")

            elif method_name == "Проверка сокращенного на целое":
                result = first_number.INT_Q_B()
                if result: self.result_label.config(text=f"Является целым")
                else: self.result_label.config(text=f"Не является целым")

            elif method_name == "Целое -> дробное":
                try:
                    first_number = get_Integer(first_number_str)
                except ValueError:
                    messagebox.showerror("Ошибка", "Первое число должно быть целым.")
                    return
                result = Rational.TRANS_Z_Q(first_number)
                self.result_label.config(text=f"Результат: {result}")


            elif method_name == "Дробное -> целое":
                result = first_number.TRANS_Q_Z()
                self.result_label.config(text=f"Результат: {result}")




if __name__ == "__main__":
    root = tk.Tk()
    app = RationalApp(root)
    root.mainloop()