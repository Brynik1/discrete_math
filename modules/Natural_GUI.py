import tkinter as tk
from tkinter import messagebox
from Natural import *


class NaturalApp:
    def __init__(self, root):
        # Определение цветов
        self.bg_color = "#1e1f22"  # Цвет фона
        self.window_color = "#2b2d30"  # Цвет окон
        self.text_color = "white"  # Цвет текста
        self.hover_color = "#3c3f42"  # Цвет при наведении

        self.root = root
        self.root.title("Natural Number Operations")
        self.root.geometry("374x420")
        self.root.configure(bg=self.bg_color)
        self.root.attributes('-alpha', 0.98)

        self.method_var = tk.StringVar(value="Сложение двух чисел")

        # Заголовок
        title_label = tk.Label(root, text="Операции с натуральными числами", bg=self.bg_color, fg=self.text_color, font=("Arial", 16))
        title_label.pack(pady=10)

        # Выбор метода
        methods = [
            "Сравнение чисел",
            "Проверка на ноль",
            "Прибавление единицы",
            "Сложение двух чисел",
            "Вычитание двух чисел",
            "Умножение на цифру",
            "Умножение на 10^k",
            "Умножение двух чисел",
            "Вычитание умноженного на цифру",
            "DIV_NN_Dk",
            "Деление целочисленное",
            "Деление с остатком",
            "НОД",
            "НОК"
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

    def calculate(self):
        method_name = self.method_var.get()
        first_number_str = self.first_number_entry.get()

        if not is_Natural(first_number_str):
            messagebox.showerror("Ошибка", "Первое число должно быть натуральным.")
            return

        first_number = Natural(first_number_str)

        if method_name in ["Сравнение чисел",
                           "Сложение двух чисел",
                           "Вычитание двух чисел",
                           "Умножение двух чисел",
                           "Вычитание умноженного на цифру",
                           "DIV_NN_Dk",
                           "Деление целочисленное",
                           "Деление с остатком",
                           "НОД",
                           "НОК"]:
            second_number_str = self.second_number_entry.get()
            if not is_Natural(second_number_str):
                messagebox.showerror("Ошибка", "Второе число должно быть натуральным.")
                return

            second_number = Natural(second_number_str)

            if method_name == "Сравнение чисел":
                comparison_result = first_number.COM_NN_D(second_number)
                comparison_texts = {
                    2: f"{first_number} больше {second_number}",
                    1: f"{first_number} меньше {second_number}",
                    0: f"{first_number} равно {second_number}"
                }
                self.result_label.config(text=comparison_texts[comparison_result])

            elif method_name == "Сложение двух чисел":
                result = first_number.ADD_NN_N(second_number)
                self.result_label.config(text=f"Результат: {result}")

            elif method_name == "Вычитание двух чисел":
                try:
                    result = first_number.SUB_NN_N(second_number)
                    self.result_label.config(text=f"Результат: {result}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", str(e))
                    return

            elif method_name == "Умножение двух чисел":
                result = first_number.MUL_NN_N(second_number)
                self.result_label.config(text=f"Результат: {result}")

            elif method_name == "Вычитание умноженного на цифру":
                digit_str = self.digit_entry.get()
                if not digit_str.isdigit() or not (0 <= int(digit_str) <= 9):
                    messagebox.showerror("Ошибка", "Цифра должна быть от 0 до 9.")
                    return
                digit = int(digit_str)
                print(digit)
                try:
                    result = first_number.SUB_NDN_N(second_number, digit)
                    self.result_label.config(text=f"Результат: {result}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", "Результат должен быть натуральным.")
                    return

            elif method_name == "DIV_NN_Dk":
                k_str = self.digit_entry.get()
                if not k_str.isdigit():
                    messagebox.showerror("Ошибка", "k должно быть неотрицательным целым числом.")
                    return
                k = int(k_str)
                try:
                    result = first_number.DIV_NN_Dk(second_number, k)
                    self.result_label.config(text=f"Результат: {result}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", str(e))
                    return

            elif method_name == "Деление целочисленное":
                result = first_number.DIV_NN_N(second_number)
                self.result_label.config(text=f"Результат: {result}")

            elif method_name == "Деление с остатком":
                result = first_number.MOD_NN_N(second_number)
                self.result_label.config(text=f"Результат: {result}")

            elif method_name == "НОД":
                result = first_number.GCF_NN_N(second_number)
                self.result_label.config(text=f"Результат: {result}")

            elif method_name == "НОК":
                result = first_number.LCM_NN_N(second_number)
                self.result_label.config(text=f"Результат: {result}")



        else:
            if method_name == "Прибавление единицы":
                result = first_number.ADD_1N_N()
                self.result_label.config(text=f"Результат: {result}")

            elif method_name == "Проверка на ноль":
                is_non_zero = first_number.NZER_N_B()
                if is_non_zero:
                    self.result_label.config(text=f"{first_number} не равно нулю")
                else:
                    self.result_label.config(text=f"{first_number} равно нулю")

            elif method_name == "Умножение на цифру":
                digit_str = self.digit_entry.get()
                if not digit_str.isdigit() or not (0 <= int(digit_str) <= 9):
                    messagebox.showerror("Ошибка", "Цифра должна быть от 0 до 9.")
                    return
                digit = int(digit_str)
                try:
                    result = first_number.MUL_ND_N(digit)
                    self.result_label.config(text=f"Результат: {result}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", str(e))
                    return

            elif method_name == "Умножение на 10^k":
                digit_str = self.digit_entry.get()
                if not digit_str.isdigit() or not (0 <= int(digit_str) <= 9):
                    messagebox.showerror("Ошибка", "Цифра должна быть от 0 до 9.")
                    return
                digit = int(digit_str)
                try:
                    result = first_number.MUL_Nk_N(digit)
                    self.result_label.config(text=f"Результат: {result}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", str(e))
                    return


if __name__ == "__main__":
    root = tk.Tk()
    app = NaturalApp(root)
    root.mainloop()
