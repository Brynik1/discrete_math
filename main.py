import tkinter as tk
import subprocess
import json
import os

class App:
    def __init__(self, root):
        # Определяем цвета темы
        self.dark_theme = {
            "bg": "#272830",
            "title": "#FFFFFF",
            "button_bg": "#3e404d",
            "button_fg": "#FFFFFF",
            "button_hover": "#80839c"
        }

        self.light_theme = {
            "bg": "#FFFFFF",
            "title": "#2e2e2e",
            "button_bg": "#DDDDDD",
            "button_fg": "#000000",
            "button_hover": "#AAAAAA"
        }

        # Загружаем сохраненную тему или устанавливаем темную тему по умолчанию
        self.current_theme = self.load_theme() or self.dark_theme

        # Создание окна
        self.root = root
        self.root.title("Выбор модуля")
        self.root.geometry("400x300")
        self.root.configure(bg=self.current_theme["bg"])
        self.root.attributes('-alpha', 1)
        self.root.resizable(False, False)

        # Заголовок
        self.title_label = tk.Label(root, text="Выберите модуль", bg=self.current_theme["bg"],
                                    fg=self.current_theme["title"], font=("Arial", 16))
        self.title_label.pack(pady=20)

        # Кнопки
        self.create_button("Модуль натуральных чисел", self.run_file1)
        self.create_button("Модуль целых чисел", self.run_file2)
        self.create_button("Модуль рациональных чисел", self.run_file3)
        self.create_button("Модуль многочленов", self.run_file4)

        # Кнопка для смены темы
        self.theme_button = tk.Button(self.root, text="☀", command=self.toggle_theme,
                                      bg=self.current_theme["bg"], fg=self.current_theme["button_fg"],
                                      font=("Arial", 14), relief=tk.FLAT, width=3, height=1, anchor=tk.CENTER)
        # Позиционируем кнопку в правом верхнем углу
        self.theme_button.place(x=350, y=10)
        self.theme_button.tkraise()
        self.theme_button.bind("<Enter>", lambda e: self.theme_button.config(bg=self.current_theme["button_hover"]))
        self.theme_button.bind("<Leave>", lambda e: self.theme_button.config(bg=self.current_theme["bg"]))

    def create_button(self, text, command):
        button = tk.Button(self.root, text=text, command=command,
                           bg=self.current_theme["button_bg"], fg=self.current_theme["button_fg"],
                           font=("Arial", 12), relief=tk.FLAT)

        button.pack(pady=10, padx=20, fill=tk.X)

        # Привязываем события наведения мыши
        button.bind("<Enter>", lambda e: button.config(bg=self.current_theme["button_hover"]))
        button.bind("<Leave>", lambda e: button.config(bg=self.current_theme["button_bg"]))

    def toggle_theme(self):
        # Меняем тему
        if self.current_theme == self.dark_theme:
            self.current_theme = self.light_theme
        else:
            self.current_theme = self.dark_theme

        # Сохраняем текущую тему
        self.save_theme()

        # Обновляем цвета интерфейса
        self.update_colors()

    def update_colors(self):
        # Обновляем цвета всех элементов интерфейса
        self.root.configure(bg=self.current_theme["bg"])
        self.title_label.configure(bg=self.current_theme["bg"], fg=self.current_theme["title"])

        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg=self.current_theme["button_bg"], fg=self.current_theme["button_fg"])

    def save_theme(self):
        # Сохраняем текущую тему в файл
        theme_name = 'light' if self.current_theme == self.light_theme else 'dark'
        with open('modules/theme.json', 'w') as f:
            json.dump({"theme": theme_name}, f)

    def load_theme(self):

        # Загружаем тему из файла, если он существует
        if os.path.exists('modules/theme.json'):
            with open('modules/theme.json', 'r') as f:
                data = json.load(f)
                if data.get("theme") == 'light':
                    return self.light_theme
                else:
                    return self.dark_theme
        return None

    def run_file1(self):
        file_path = "modules/Natural_GUI.py"  # Укажите путь к вашему файлу
        theme = 'light' if self.current_theme == self.light_theme else 'dark'  # Определяем текущую тему
        self.run_file(file_path, theme)

    def run_file2(self):
        file_path = "modules/Integer_GUI.py"  # Укажите путь к вашему файлу
        theme = 'light' if self.current_theme == self.light_theme else 'dark'  # Определяем текущую тему
        self.run_file(file_path, theme)

    def run_file3(self):
        file_path = "modules/Rational_GUI.py"  # Укажите путь к вашему файлу
        theme = 'light' if self.current_theme == self.light_theme else 'dark'  # Определяем текущую тему
        self.run_file(file_path, theme)

    def run_file4(self):
        file_path = "modules/Polynomial_GUI.py"  # Укажите путь к вашему файлу
        theme = 'light' if self.current_theme == self.light_theme else 'dark'  # Определяем текущую тему
        self.run_file(file_path, theme)

    def run_file(self, file_path, theme='dark'):
        # Проверка существования файла перед его запуском
        if os.path.exists(file_path):
            # Запуск файла с передачей аргумента темы
            subprocess.Popen(["python", file_path, "--theme", theme], creationflags=subprocess.CREATE_NO_WINDOW)
        else:
            print(f"Файл {file_path} не найден.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
