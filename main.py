import tkinter as tk
import subprocess
import os

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Выбор модуля")
        self.root.geometry("400x300")
        self.root.configure(bg="#2E2E2E")  # Темный фон

        # Заголовок
        self.title_label = tk.Label(root, text="Выберите модуль", bg="#2E2E2E", fg="#FFFFFF", font=("Arial", 16))
        self.title_label.pack(pady=20)

        # Кнопка 1
        self.button1 = tk.Button(root, text="Модуль натуральных чисел", command=self.run_file1, bg="#4B4B4B", fg="#FFFFFF", font=("Arial", 12), relief=tk.FLAT)
        self.button1.pack(pady=10, padx=20, fill=tk.X)

        # Кнопка 2
        self.button2 = tk.Button(root, text="Модуль целых чисел", command=self.run_file2, bg="#4B4B4B", fg="#FFFFFF", font=("Arial", 12), relief=tk.FLAT)
        self.button2.pack(pady=10, padx=20, fill=tk.X)

        # Кнопка 3
        self.button3 = tk.Button(root, text="Модуль рациональных чисел", command=self.run_file3, bg="#4B4B4B", fg="#FFFFFF", font=("Arial", 12), relief=tk.FLAT)
        self.button3.pack(pady=10, padx=20, fill=tk.X)

        # Кнопка 4
        self.button4 = tk.Button(root, text="Модуль многочленов", command=self.run_file4, bg="#4B4B4B", fg="#FFFFFF", font=("Arial", 12), relief=tk.FLAT)
        self.button4.pack(pady=10, padx=20, fill=tk.X)

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

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
