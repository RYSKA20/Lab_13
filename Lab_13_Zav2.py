import tkinter as tk
from math import cos, tan, floor

# Оголошення функції для обчислення значення
def calculate_function(event=None):
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        numerator = 3 * cos(a + b * c)
        denominator = (1 / tan(c - b)) + a ** 3
        result = numerator / denominator + floor(c / b)

        formatted_result = "{:.2f}".format(result)
        label_result.config(text="Результат: " + formatted_result)
    except ValueError:
        label_result.config(text="Помилка: введіть числа!")
    except ZeroDivisionError:
        label_result.config(text="Помилка: ділення на нуль!")
    except Exception as e:
        label_result.config(text="Інша помилка: " + str(e))

# Ініціалізація графічного вікна
root = tk.Tk()
root.title("Обчислення функції")
root.geometry("600x300")

# Додавання зображення
label_image = tk.Label()
try:
    photo = tk.PhotoImage(file="Завдання 2.png")
    label_image.configure(image=photo)
except:
    label_image.config(text="Зображення не знайдено.")
label_image.grid(row=0, column=0, columnspan=2, pady=10)

# Поля для введення a, b, c
label_a = tk.Label(root, text="Введіть значення a:")
label_a.grid(row=1, column=0, sticky="e", padx=10, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=1, column=1, padx=10, pady=5)

label_b = tk.Label(root, text="Введіть значення b:")
label_b.grid(row=2, column=0, sticky="e", padx=10, pady=5)
entry_b = tk.Entry(root)
entry_b.grid(row=2, column=1, padx=10, pady=5)

label_c = tk.Label(root, text="Введіть значення c:")
label_c.grid(row=3, column=0, sticky="e", padx=10, pady=5)
entry_c = tk.Entry(root)
entry_c.grid(row=3, column=1, padx=10, pady=5)

# Кнопка для обчислення
button_calculate = tk.Button(root, text="Обчислити", command=calculate_function)
button_calculate.grid(row=4, column=0, columnspan=2, pady=10)

# Відображення результату
label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.grid(row=5, column=0, columnspan=2)

# Додати можливість обчислення при натисканні Enter
root.bind('<Return>', calculate_function)

# Запуск GUI
root.mainloop()