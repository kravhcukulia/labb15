# 1. Імпортуй графічну бібліотеку tkinter.
import tkinter as tk

# 2. Імпортуйте модуль для роботи з системними діалоговими вікнами
from tkinter import filedialog

# 3. Імпортуйте додаткові модулі для виклику вікна повідомлення, кольору
from tkinter import messagebox, colorchooser

# 4. Створи головне вікно.
root = tk.Tk()
root.title("Блокнот")
root.geometry("800x600")

# 5. Створіть головне меню
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# 6. Створіть текстову область
text_area = tk.Text(root, undo=True)
text_area.pack(fill=tk.BOTH, expand=True)

# 7-8. Пункт меню Файл
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)

# 12. Створіть функцію new_file().
def new_file():
    text_area.delete(1.0, tk.END)

# 13. Додайте пункт Новий
file_menu.add_command(label="Новий", command=new_file)

# 14. Функція для відкриття файлу
def open_file():
    file = filedialog.askopenfile(mode="r")
    if file is not None:
        content = file.read()
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.END, content)
        file.close()

# 15. Додайте пункт Відкрити
file_menu.add_command(label="Відкрити", command=open_file)

# 16. Функція для збереження файлу
def save_file():
    file = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    if file is not None:
        content = text_area.get(1.0, tk.END)
        file.write(content)
        file.close()

# 17. Додайте пункт Зберегти
file_menu.add_command(label="Зберегти", command=save_file)

# 18. Функція для виходу
def exit_app():
    if messagebox.askyesno("Закрити", "Закрити програму?"):
        root.destroy()

file_menu.add_separator()
file_menu.add_command(label="Вихід", command=exit_app)

# 19. Зміна кольорів
def change_text_color():
    color = colorchooser.askcolor(color=text_area["fg"])[1]
    if color:
        text_area.configure(fg=color)

def change_background_color():
    color = colorchooser.askcolor(color=text_area["bg"])[1]
    if color:
        text_area.configure(bg=color)

# 20. Меню Формат
format_menu = tk.Menu(menu_bar, tearoff=0)
format_menu.add_command(label="Колір тексту", command=change_text_color)
format_menu.add_command(label="Колір фону", command=change_background_color)
menu_bar.add_cascade(label="Формат", menu=format_menu)

# 21. Функції для редагування
def cut_text():
    text_area.event_generate("<<Cut>>")

def copy_text():
    text_area.event_generate("<<Copy>>")

def paste_text():
    text_area.event_generate("<<Paste>>")

# 22. Меню Редагувати
edit_menu = tk.Menu(menu_bar, tearoff=0)
edit_menu.add_command(label="Вирізати", command=cut_text)
edit_menu.add_command(label="Копіювати", command=copy_text)
edit_menu.add_command(label="Вставити", command=paste_text)
menu_bar.add_cascade(label="Редагувати", menu=edit_menu)

# 23. Функції Довідки
def show_about():
    messagebox.showinfo("Про програму", "Це простий текстовий редактор.")

def show_help():
    messagebox.showinfo("Про автора", "Автор: Кравчук Юлія")

# 24. Меню Довідка
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Про програму", command=show_about)
help_menu.add_command(label="Про автора", command=show_help)
menu_bar.add_cascade(label="Довідка", menu=help_menu)

# 25. Контекстне меню
context_menu = tk.Menu(root, tearoff=0)
context_menu.add_command(label="Колір тексту", command=change_text_color)
context_menu.add_command(label="Колір фону", command=change_background_color)
context_menu.add_command(label="Зберегти", command=save_file)

def show_context_menu(event):
    context_menu.tk_popup(event.x_root, event.y_root)

text_area.bind("<Button-3>", show_context_menu)

# Запуск головного циклу
root.mainloop()

