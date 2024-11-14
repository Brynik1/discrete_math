from modules.Natural_GUI import create_NaturalApp
from modules.Integer_GUI import create_IntegerApp
from modules.Rational_GUI import create_RationalApp
from modules.Polynomial_GUI import create_PolynomialApp
import datetime
import tkinter as tk
import json

class App:
    def __init__(self, root):
        # Определяем цвета тем
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

        self.pink_theme = {
            "bg": "#fcc1c0",  # Розовый фон
            "title": "#A50000",  # Белый текст заголовка
            "button_bg": "#ffe3e3",  # Ярко-розовые кнопки
            "button_fg": "red",  # Белый текст на кнопках
            "button_hover": "#ffffff"  # Темно-розовый при наведении
        }

        # Загружаем сохраненную тему или устанавливаем темную тему по умолчанию
        self.current_theme = self.load_theme() or self.dark_theme

        # Создание окна
        self.root = root
        self.root.title("Выбор модуля")
        self.root.geometry("400x280")
        self.root.configure(bg=self.current_theme["bg"])
        self.root.attributes('-alpha', 1)
        self.root.resizable(False, False)
        self.counter = 0

        # Заголовок
        self.title_label = tk.Label(root, text="Выберите модуль", bg=self.current_theme["bg"],
                                     fg=self.current_theme["title"], font=("Arial", 18))
        self.title_label.pack(pady=20)

        # Кнопки
        self.create_button("Модуль натуральных чисел", self.run_file1)
        self.create_button("Модуль целых чисел", self.run_file2)
        self.create_button("Модуль рациональных чисел", self.run_file3)
        self.create_button("Модуль многочленов", self.run_file4)

        # Кнопка для смены темы
        self.theme_button = tk.Button(self.root, text="☀", command=self.toggle_theme,
                                      bg=self.current_theme["bg"], fg=self.current_theme["button_fg"],
                                      font=("Arial", 15), relief=tk.FLAT, width=3, height=1, anchor=tk.CENTER)

        # Позиционируем кнопку в правом верхнем углу
        self.theme_button.place(x=350, y=10)
        self.theme_button.tkraise()
        self.theme_button.bind("<Enter>", lambda e: self.theme_button.config(bg=self.current_theme["button_hover"]))
        self.theme_button.bind("<Leave>", lambda e: self.theme_button.config(bg=self.current_theme["bg"]))

    def create_button(self, text, command):
        button = tk.Button(self.root, text=text, command=command,
                           bg=self.current_theme["button_bg"], fg=self.current_theme["button_fg"],
                           font=("Arial", 12), relief=tk.FLAT)

        button.pack(pady=8, padx=15, fill=tk.X)

        # Привязываем события наведения мыши
        button.bind("<Enter>", lambda e: button.config(bg=self.current_theme["button_hover"]))
        button.bind("<Leave>", lambda e: button.config(bg=self.current_theme["button_bg"]))

    def toggle_theme(self):
        # Меняем тему по кругу
        self.counter += 1
        if self.counter > 10:
            if self.current_theme == self.dark_theme:
                self.current_theme = self.light_theme
            elif self.current_theme == self.light_theme:
                self.current_theme = self.pink_theme
            else:
                self.current_theme = self.dark_theme
        else:
            if self.current_theme == self.dark_theme:
                self.current_theme = self.light_theme
            else:
                self.current_theme = self.dark_theme


        # Обновляем цвета интерфейса
        self.update_colors()

        # Сохраняем текущую тему
        self.save_theme()

    def update_colors(self):
        # Обновляем цвета всех элементов интерфейса
        self.root.configure(bg=self.current_theme["bg"])
        self.title_label.configure(bg=self.current_theme["bg"], fg=self.current_theme["title"])
        if self.current_theme == self.pink_theme:
            # Получаем текущее системное время
            current_time = datetime.datetime.now()
            current_hour = current_time.hour
            # Определяем пожелание в зависимости от времени суток
            if 5 <= current_hour < 12: greeting = "С доброй утрой"
            elif 12 <= current_hour < 18: greeting = "С доброй днёй"
            else: greeting = "С доброй вечерой"
            self.theme_button.config(text='♥')
            self.title_label['text'] = greeting + "  ʕ ᵔᴥᵔ ʔ"
        else:
            self.theme_button.config(text="☀")
            self.title_label['text'] = "Выберите модуль"
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget.configure(bg=self.current_theme["button_bg"], fg=self.current_theme["button_fg"])
                #if self.current_theme == self.pink_theme and widget != self.theme_button:
                #    widget['text'] = widget['text'] + '  (^･ｪ･^)'
                #elif widget != self.theme_button and '(^･ｪ･^)' in widget['text']:
                #    widget['text'] = widget['text'][:-9]


    def save_theme(self):
        # Сохраняем текущую тему в файл
        try:
            if self.current_theme == self.light_theme: theme_name = 'light'
            elif self.current_theme == self.pink_theme: theme_name = 'pink'
            else: theme_name = 'dark'
            with open('theme.json', 'w') as f:
                json.dump({"theme": theme_name}, f)
        except:
            return

    def load_theme(self):
        try:
            with open('theme.json', 'r') as f:
                data = json.load(f)
                if data.get("theme") == 'light': return self.light_theme
                else: return self.dark_theme
        except:
            return None

    def run_file1(self):
        if self.current_theme == self.light_theme: theme = 'light'
        elif self.current_theme == self.pink_theme: theme = 'pink'
        else: theme = 'dark'
        window = create_NaturalApp(root, theme)

    def run_file2(self):
        if self.current_theme == self.light_theme: theme = 'light'
        elif self.current_theme == self.pink_theme: theme = 'pink'
        else: theme = 'dark'
        window = create_IntegerApp(root, theme)

    def run_file3(self):
        if self.current_theme == self.light_theme:
            theme = 'light'
        elif self.current_theme == self.pink_theme:
            theme = 'pink'
        else:
            theme = 'dark'
        window = create_RationalApp(root, theme)

    def run_file4(self):
        if self.current_theme == self.light_theme:
            theme = 'light'
        elif self.current_theme == self.pink_theme:
            theme = 'pink'
        else:
            theme = 'dark'
        window = create_PolynomialApp(root, theme)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
