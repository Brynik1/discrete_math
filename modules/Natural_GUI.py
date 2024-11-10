import tkinter as tk
from tkinter import messagebox
from Natural import *
from additionally import *
import argparse


class NaturalApp:
    def __init__(self, root, theme='dark'):
        # Определение цветов в зависимости от темы
        if theme == 'light':
            self.bg_color = "#FFFFFF"  # Цвет фона
            self.window_color = "#EAEAEA"  # Цвет окон
            self.text_color = "#2e2e2e"  # Цвет текста
            self.hover_color = "#c991d3"  # Цвет при наведении
            self.button_color = "#9966CC"  # Цвет для кнопки
            self.backlight = "#2e2e2e"  # Цвет подсветки текста
        else:  # Темная тема по умолчанию
            self.bg_color = "#24252b"  # Цвет фона
            self.window_color = "#3e404d"  # Цвет окон
            self.text_color = "#F5F5F5"  # Цвет текста
            self.hover_color = "#c991d3"  # Цвет при наведении
            self.button_color = "#9966CC"  # Цвет для кнопки
            self.backlight = "#F5F5F5"  # Цвет подсветки текста

        self.root = root
        self.root.title("Natural Operations")
        self.root.geometry("360x420")
        self.root.configure(bg=self.bg_color)
        self.root.attributes('-alpha', 1)

        self.method_var = tk.StringVar(value="Сложение двух чисел")

        # Заголовок
        title_label = tk.Label(root, text="Операции с натуральными", bg=self.bg_color, fg=self.text_color, font=("Arial", 16))
        title_label.pack(pady=10)

        # Выбор метода
        methods = [
            "Сравнение чисел",
            "Проверка на ноль",
            "Прибавление единицы",
            "Сложение двух чисел",
            "Вычитание двух чисел",
            "Умножение на цифру",
            "Умножение на 10ⁿ",
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
        self.first_number_label = tk.Label(root, text="✔ Введите первое число:", bg=self.bg_color, fg=self.backlight, font=("Arial", 10))
        self.first_number_label.pack(pady=5)
        self.first_number_entry = tk.Entry(root, bg=self.window_color, fg=self.text_color, width=26, insertbackground='black' if theme == 'light' else 'white', font=("Arial", 14))
        self.first_number_entry.pack(pady=5)

        # Ввод второго числа
        self.second_number_label = tk.Label(root, text="✔ Введите второе число:", bg=self.bg_color, fg=self.backlight, font=("Arial", 10))
        self.second_number_label.pack(pady=5)
        self.second_number_entry = tk.Entry(root, bg=self.window_color, fg=self.text_color, width=26, insertbackground='black' if theme == 'light' else 'white', font=("Arial", 14))
        self.second_number_entry.pack(pady=5)

        # Ввод цифры
        self.digit_label = tk.Label(root, text="Введите цифру:", bg=self.bg_color, fg=self.text_color, font=("Arial", 10))
        self.digit_label.pack(pady=5)
        self.digit_entry = tk.Entry(root, bg=self.window_color, fg=self.text_color, width=10, insertbackground='black' if theme == 'light' else 'white', font=("Arial", 14))
        self.digit_entry.pack(pady=5)

        # Метка для результата
        self.result_label = tk.Label(root, text="", bg=self.bg_color, fg=self.text_color, font=("Arial", 14))
        self.result_label.pack(pady=10)

        # Кнопка для выполнения операции
        self.calculate_button = tk.Button(root, text="Выполнить", command=self.calculate, bg=self.button_color, fg="white", font=("Arial", 14), height=1, width=15, relief=tk.FLAT)
        self.calculate_button.place(relx=0.5, y=380, anchor=tk.CENTER)
        self.calculate_button.bind("<Enter>", lambda e: self.calculate_button.config(bg=self.hover_color))
        self.calculate_button.bind("<Leave>", lambda e: self.calculate_button.config(bg=self.button_color))

    def to_superscript(self, n):
        superscripts = {
            '0': '⁰', '1': '¹', '2': '²', '3': '³',
            '4': '⁴', '5': '⁵', '6': '⁶', '7': '⁷',
            '8': '⁸', '9': '⁹'
        }
        return ''.join(superscripts[digit] for digit in str(n))

    def on_option_change(self, value):
        method_name = self.method_var.get()
        self.second_number_label.config(fg=self.text_color, text="Введите второе число:")
        self.digit_label.config(fg=self.text_color, text="Введите цифру:")
        if method_name in ["Сравнение чисел",
                           "Сложение двух чисел",
                           "Вычитание двух чисел",
                           "Умножение двух чисел",
                           "DIV_NN_Dk",
                           "Деление целочисленное",
                           "Деление с остатком",
                           "НОД",
                           "НОК",
                           "Вычитание умноженного на цифру"]:
            self.second_number_label.config(fg=self.backlight, text="✔ Введите второе число:")
            if method_name == "Вычитание умноженного на цифру":
                self.digit_label.config(fg=self.backlight, text="✔ Введите цифру:")

        else:
            if method_name in ["Проверка на ноль", "Прибавление единицы"]:
                return
            else:
                self.digit_label.config(fg=self.backlight, text="✔ Введите цифру:")

    def calculate(self):
        self.result_label.config(text='', fg=self.text_color, font=("Arial", 14))
        method_name = self.method_var.get()
        first_number_str = self.first_number_entry.get()

        try:
            first_number = get_Natural(first_number_str)
        except ValueError:
            if first_number_str == '':
                messagebox.showerror("Ошибка", f"Первое число не введено.")
            else:
                messagebox.showerror("Ошибка", f"Первое число должно быть натуральным.")
            return

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

            try:
                second_number = get_Natural(second_number_str)
            except ValueError:
                if second_number_str == '':
                    messagebox.showerror("Ошибка", f"Второе число не введено.")
                else:
                    messagebox.showerror("Ошибка", f"Второе число должно быть натуральным.")
                return

            if method_name == "Сравнение чисел":
                comparison_result = first_number.COM_NN_D(second_number)
                comparison_texts = {
                    2: f"{first_number} > {second_number}",
                    1: f"{first_number} < {second_number}",
                    0: f"{first_number} == {second_number}"
                }
                self.result_label.config(text=comparison_texts[comparison_result])

            elif method_name == "Сложение двух чисел":
                result = first_number.ADD_NN_N(second_number)
                self.result_label.config(text=f"{first_number} + {second_number} = {result}")

            elif method_name == "Вычитание двух чисел":
                try:
                    result = first_number.SUB_NN_N(second_number)
                    self.result_label.config(text=f"{first_number} - {second_number} = {result}")
                except ValueError:
                    messagebox.showerror("Ошибка", f"Результат должен быть натуральным.")
                    return

            elif method_name == "Умножение двух чисел":
                result = first_number.MUL_NN_N(second_number)
                self.result_label.config(text=f"{first_number} ∙ {second_number} = {result}")

            elif method_name == "Вычитание умноженного на цифру":
                digit_str = self.digit_entry.get()
                if not digit_str.isdigit() or not (0 <= int(digit_str) <= 9):
                    messagebox.showerror("Ошибка", "Цифра должна быть от 0 до 9.")
                    return
                digit = int(digit_str)
                try:
                    result = first_number.SUB_NDN_N(second_number, digit)
                    self.result_label.config(text=f"{first_number} - {second_number}∙{digit} = {result}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", "Результат должен быть натуральным.")
                    return

            elif method_name == "DIV_NN_Dk":
                k_str = self.digit_entry.get()
                if k_str == '' or not all(c.isdigit() for c in k_str):
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
                self.result_label.config(text=f"{first_number} div {second_number} = {result}")

            elif method_name == "Деление с остатком":
                result = first_number.MOD_NN_N(second_number)
                self.result_label.config(text=f"{first_number} mod {second_number} = {result}")

            elif method_name == "НОД":
                result = first_number.GCF_NN_N(second_number)
                self.result_label.config(text=f"НОД{chr(0x202F)}({first_number};{chr(0x202F)}{second_number}) = {result}")

            elif method_name == "НОК":
                result = first_number.LCM_NN_N(second_number)
                self.result_label.config(text=f"НОК{chr(0x202F)}({first_number};{chr(0x202F)}{second_number}) = {result}")


        else:
            if method_name == "Прибавление единицы":
                result = first_number.ADD_1N_N()
                self.result_label.config(text=f"{first_number} + 1 = {result}")

            elif method_name == "Проверка на ноль":
                is_non_zero = first_number.NZER_N_B()
                if is_non_zero:
                    self.result_label.config(text=f"{first_number} ≠ 0")
                else:
                    self.result_label.config(text=f"{first_number} = 0")

            elif method_name == "Умножение на цифру":
                digit_str = self.digit_entry.get()
                if digit_str == '' or not digit_str.isdigit() or not (0 <= int(digit_str) <= 9):
                    messagebox.showerror("Ошибка", "Цифра должна быть от 0 до 9.")
                    return
                digit = int(digit_str)
                try:
                    result = first_number.MUL_ND_N(digit)
                    self.result_label.config(text=f"{first_number} ∙ {digit} = {result}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", str(e))
                    return

            elif method_name == "Умножение на 10ⁿ":
                digit_str = self.digit_entry.get()
                try:
                    get_Natural(digit_str)
                    digit = int(digit_str)
                except ValueError:
                    second_number_str = self.second_number_entry.get()
                    try:
                        get_Natural(second_number_str)
                        digit = int(second_number_str)
                    except ValueError:
                        messagebox.showerror("Ошибка", "Степень должна быть натуральным числом.")
                        return
                try:
                    result = first_number.MUL_Nk_N(digit)
                    self.result_label.config(text=f"{first_number} ∙ 10{self.to_superscript(digit)} = {result}")
                except ValueError as e:
                    messagebox.showerror("Ошибка", str(e))
                    return


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Polynomial Operations App')
    parser.add_argument('--theme', type=str, choices=['light', 'dark'], default='dark',
                        help='Choose the theme of the application')

    args = parser.parse_args()

    root = tk.Tk()
    app = NaturalApp(root, theme=args.theme)  # Передача темы из аргументов командной строки
    root.mainloop()