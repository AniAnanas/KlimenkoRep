"""Вариант 14. => 14Var.png"""
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

PLACEHOLDER = "https://"
NOT_SELECTED_TEXT = "Не выбрано"
branch_options: list[str] = ["select B1", "select B2", "select B3", "select B4"]
degree_options: list[str] = ["select D1", "select D2", "select D3", "select D4"]
prev_rb_var = -1

degree_choice = tk.IntVar(value=-1)

def focus_next(event):
    event.widget.tk_focusNext().focus()
    return "break"

def on_select(event):
    val = event.widget.get()
    if val:
        print(val)
        return focus_next(event)
    print(messagebox.showerror("Ошибка!", "Поле не должно быть пустым!"))
    return

def rb_changed():
    global prev_rb_var
    val = degree_choice.get()
    if prev_rb_var != val:
        print(val)
        prev_rb_var = val
    return

def empty_obj(root,row,col):
    tk.Label(root, text="").grid(row=row, column=col, padx=10, pady=10)

root = tk.Tk()
root.title("Registration Details")

def Uniiversity():
    uni_label = tk.Label(root, text="University:")
    uni_label.grid(row=0, column=0, padx=10, pady=10)

    uni_entry = tk.Entry(root)
    uni_entry.grid(row=0, column=1, columnspan=4, sticky="we", padx=10, pady=10)
    uni_entry.bind("<Return>", on_select)
    uni_entry.focus() #Фокус в самом начале
Uniiversity()

def Institute():
    inst_label = tk.Label(root, text="Institute:")
    inst_label.grid(row=1, column=0, padx=10, pady=10)

    inst_entry = tk.Entry(root)
    inst_entry.grid(row=1, column=1, columnspan=4, sticky="we", padx=10, pady=10)
    inst_entry.bind("<Return>", on_select)
Institute()

def Branch():
    branch_label = tk.Label(root, text="Branch:")
    branch_label.grid(row=2, column=0, padx=10, pady=10)

    branch_combo = ttk.Combobox(root, values=branch_options, justify="center")
    branch_combo.grid(row=2, column=1, columnspan=3, sticky="we", padx=10, pady=10)
    branch_combo.set(NOT_SELECTED_TEXT)
    branch_combo.bind("<<ComboboxSelected>>", on_select)
Branch()

def Degree():
    degree_label = tk.Label(root, text="Degree:")
    degree_label.grid(row=3, column=0, padx=10, pady=10)

    degree_combo = ttk.Combobox(root, values=degree_options, justify="center")
    degree_combo.grid(row=3, column=1, columnspan=2, sticky="we", padx=10, pady=10)
    degree_combo.set(NOT_SELECTED_TEXT)
    degree_combo.bind("<<ComboboxSelected>>", on_select)

    degree_radio1 = tk.Radiobutton(root, text="Pursuing", value=0, variable=degree_choice, command=rb_changed)
    degree_radio1.grid(row=3, column=3, columnspan=1, padx=2, pady=10)

    degree_radio2 = tk.Radiobutton(root, text="Completed", value=1, variable=degree_choice, command=rb_changed)
    degree_radio2.grid(row=3, column=4, columnspan=1, padx=2, pady=10)
Degree()

def CPI():
    cpi_label1 = tk.Label(root, text="Average CPI:")
    cpi_label1.grid(row=4, column=0, padx=10, pady=10)

    cpi_spin1 = tk.Spinbox(root, from_=0, to=10)
    cpi_spin1.grid(row=4, column=1, columnspan=1, sticky="we", padx=2, pady=10)
    cpi_spin1.bind("<Return>", on_select)

    cpi_label2 = tk.Label(root, text="Up to")
    cpi_label2.grid(row=4, column=2, columnspan=1, sticky="we", padx=2, pady=10)

    cpi_spin2 = tk.Spinbox(root, from_=0, to=10)
    cpi_spin2.grid(row=4, column=3, columnspan=1, sticky="we", padx=2, pady=10)
    cpi_spin2.bind("<Return>", on_select)

    cpi_label3 = tk.Label(root, text="Th Semester")
    cpi_label3.grid(row=4, column=4, columnspan=1, sticky="we", padx=2, pady=10)
CPI()

def Experience():
    exp_label1 = tk.Label(root, text="Experience:")
    exp_label1.grid(row=5, column=0, padx=10, pady=10)

    exp_spin = tk.Spinbox(root, from_=0, to=50)
    exp_spin.grid(row=5, column=1, columnspan=1, sticky="we", padx=2, pady=10)
    exp_spin.bind("<Return>", on_select)

    exp_label2 = tk.Label(root, text="Years")
    exp_label2.grid(row=5, column=2, columnspan=1, sticky="we", padx=2, pady=10)
Experience()

def Web():
    def _show_placeholder(event=None):
        global PLACEHOLDER
        self = event.widget
        if not self.get():
            self.delete(0, tk.END)
            self.insert(0, PLACEHOLDER)
            self['fg'] = "grey"

    def _clear_placeholder(event=None):
        global PLACEHOLDER
        self = event.widget
        if self['fg'] == "grey":
            self.delete(0, tk.END)
            self['fg'] = "black"

    web_label = tk.Label(root, text="Your Website Or Blog:")
    web_label.grid(row=6, column=0, padx=10, pady=10)
    web_entry = tk.Entry(root)
    web_entry.bind("<FocusIn>", _clear_placeholder)
    web_entry.bind("<FocusOut>", _show_placeholder)
    web_entry.bind("<Return>", on_select)

    #Показать сразу плейсхолдер
    e1 = tk.Event()
    e1.widget = web_entry
    _show_placeholder(e1)
    del e1

    web_entry.grid(row=6, column=1, columnspan=3, sticky="we", padx=10, pady=10)
Web()

root.mainloop()
