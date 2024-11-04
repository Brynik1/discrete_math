import tkinter as tk
import subprocess
import os


class App:
    def __init__(self, root):
        # Определяем цвета
        self.bg_color = "#2E2E2E"  # Темный фон
        self.title_color = "#FFFFFF"  # Цвет заголовка
        self.button_bg_color = "#4B4B4B"  # Цвет фона кнопок
        self.button_fg_color = "#FFFFFF"  # Цвет текста кнопок
        self.button_hover_color = "#808080"  # Цвет кнопок при наведении
        self.font_family = "Arial"
        self.title_font_size = 16
        self.button_font_size = 12

        # Создание окна
        self.root = root
        self.root.title("Выбор модуля")
        self.root.geometry("400x300")
        self.root.configure(bg=self.bg_color)
        self.root.attributes('-alpha', 1)
        self.root.resizable(False, False)

        # Заголовок
        self.title_label = tk.Label(root, text="Выберите модуль", bg=self.bg_color, fg=self.title_color,
                                    font=(self.font_family, self.title_font_size))
        self.title_label.pack(pady=20)

        # Кнопки
        self.create_button("Модуль натуральных чисел", self.run_file1)
        self.create_button("Модуль целых чисел", self.run_file2)
        self.create_button("Модуль рациональных чисел", self.run_file3)
        self.create_button("Модуль многочленов", self.run_file4)

    def create_button(self, text, command):
        button = tk.Button(self.root, text=text, command=command,
                           bg=self.button_bg_color, fg=self.button_fg_color,
                           font=(self.font_family, self.button_font_size), relief=tk.FLAT)

        button.pack(pady=10, padx=20, fill=tk.X)

        # Привязываем события наведения мыши
        button.bind("<Enter>", lambda e: button.config(bg=self.button_hover_color))
        button.bind("<Leave>", lambda e: button.config(bg=self.button_bg_color))

    def run_file1(self):
        file_path = "modules/Natural_GUI.py"  # Укажите путь к вашему файлу
        self.run_file(file_path)

    def run_file2(self):
        file_path = "modules/Integer_GUI.py"  # Укажите путь к вашему файлу
        self.run_file(file_path)

    def run_file3(self):
        file_path = "modules/Rational_GUI.py"  # Укажите путь к вашему файлу
        self.run_file(file_path)

    def run_file4(self):
        file_path = "modules/Polynomial_GUI.py"  # Укажите путь к вашему файлу
        self.run_file(file_path)

    def run_file(self, file_path):
        # Проверка существования файла перед его запуском
        if os.path.exists(file_path):
            subprocess.Popen(["python", file_path])  # Используйте "python3" для Linux/Mac
        else:
            print(f"Файл {file_path} не найден.")


# Запуск приложения
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
