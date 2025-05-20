import tkinter as tk
from math import cos, tan, floor

def calculate_function(event=None):
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())

    try:
        numerator = 3 * cos(a + b * c)
        denominator = (1 / tan(c - b)) + a**3
        result = numerator / denominator + floor(c / b)
        format_result = "{:.2f}".format(result)
        label_result.config(text="Результат: " + format_result)
    except Exception as e:
        label_result.config(text="Помилка: " + str(e))

root = tk.Tk()
root.title("Обчислення функції")
root.geometry("400x400")

# Зображення (опціонально)
label_image = tk.Label()
label_image.pack()
try:
    photo = tk.PhotoImage(file="Завдання 1.png")
    label_image.configure(image=photo)
except:
    pass

label_a = tk.Label(root, text="Введіть значення a:")
label_a.pack()
entry_a = tk.Entry(root)
entry_a.pack()

label_b = tk.Label(root, text="Введіть значення b:")
label_b.pack()
entry_b = tk.Entry(root)
entry_b.pack()

label_c = tk.Label(root, text="Введіть значення c:")
label_c.pack()
entry_c = tk.Entry(root)
entry_c.pack()

button_calculate = tk.Button(root, text="Обчислити")
button_calculate.pack()
button_calculate.bind('<Button-1>', calculate_function)

label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()