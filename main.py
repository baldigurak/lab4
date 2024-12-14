import tkinter as tk
from tkinter import messagebox
import random
import string


def generate_password():
    include_lowercase = lowercase_var.get()
    include_digits = digits_var.get()
    include_special = special_var.get()
    password_length = int(entry_length.get())

    characters =""

    if include_lowercase:
        characters += 'abcdefghijklmnopqrstuvwxyz'
    if include_digits:
        characters += '1234567890'
    if include_special:
        characters += '!@#$%'


    if not characters:
        messagebox.showwarning("Предупреждение", "Выберите хотя бы один параметр для генерации пароля.")
        return


    password = ''.join(random.choice(characters) for _ in range(password_length))

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)




root = tk.Tk()
root.title("Генератор паролей")

lowercase_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

label_length = tk.Label(root, text="Длина пароля:")
label_length.pack()


entry_length = tk.Entry(root)
entry_length.pack()

lowercase_check = tk.Checkbutton(root, text="Включить алфавит нижнего регистра [a-z]", variable=lowercase_var)
digits_check = tk.Checkbutton(root, text="Включить цифры [0-9]", variable=digits_var)
special_check = tk.Checkbutton(root, text="Включить спецсимволы [!@$%^]", variable=special_var)

lowercase_check.pack(anchor='w')
digits_check.pack(anchor='w')
special_check.pack(anchor='w')



generate_button = tk.Button(root, text="Сгенерировать пароль", command=generate_password)
generate_button.pack(pady=10)

password_entry = tk.Entry(root, width=40)
password_entry.pack(pady=10)

root.mainloop()
