'''Вариант 13.
    Описать функцию ShiftRight3(A, B, C), выполняющую правый циклический сдвиг:
    значение A переходит в B, значение B в C, значение C в A (A, B, C —
    вещественные параметры, являющиеся одновременно входными и выходными). С
    помощью этой функции выполнить правый циклический сдвиг для двух данных
    наборов из трех чисел: (A1, B1, C1) и (A2, B2, C2).
'''

# def shift_right3(A, B, C):
#     return C, A, B

import tkinter as tk
from tkinter import Spinbox
from re import fullmatch
from typing import Any

def check(var=str()):
    return fullmatch(r'-?\d{0,}', var) is not None

def start_shift():
    global a1, b1, c1, a2, b2, c2

    if (a1.get() == b1.get() == c1.get()): return
    if any(fieldIsNullOrEmpty(num) for num in (a1, b1, c1)): return

    last_a1 = a1.get()
    a1.set(c1.get())
    c1.set(b1.get())
    b1.set(last_a1)
    del last_a1

    #Повторяем для второй тройки чисел
    if (a2.get() == b2.get() == c2.get()): return
    if any(fieldIsNullOrEmpty(num) for num in (a2, b2, c2)): return
    
    last_a2 = a2.get()
    a2.set(c2.get())
    c2.set(b2.get())
    b2.set(last_a2)
    del last_a2


def fieldIsNullOrEmpty(a:tk.StringVar):
    try:
        if a is None:
            return True
        i = int(a.get())
    except ValueError:
        return True
    return False

def first_nums(master:tk.Tk, 
                kw_grid:dict[str, str|Any],
                kw_spin:dict[str, str|Any]):
    a1_Label = tk.Label(master, text="A1:")
    a1_Label.grid(row=0, column=0, **kw_grid)

    a1_Spin = Spinbox(master, **kw_spin, textvariable=a1)
    a1_Spin.grid(row=0, column=1, **kw_grid)

    b1_Label = tk.Label(master, text="B1:")
    b1_Label.grid(row=0, column=2, **kw_grid)

    b1_Spin = Spinbox(master, **kw_spin, textvariable=b1)
    b1_Spin.grid(row=0, column=3, **kw_grid)

    c1_Label = tk.Label(master, text="C1:")
    c1_Label.grid(row=0, column=4, **kw_grid)

    c1_Spin = Spinbox(master, **kw_spin, textvariable=c1)
    c1_Spin.grid(row=0, column=5, **kw_grid)


def second_nums(master, kw_grid, kw_spin):
    a2_Label = tk.Label(master, text="A2:")
    a2_Label.grid(row=1, column=0, **kw_grid)

    a2_Spin = Spinbox(master, **kw_spin, textvariable=a2)
    a2_Spin.grid(row=1, column=1, **kw_grid)

    b2_Label = tk.Label(master, text="B2:")
    b2_Label.grid(row=1, column=2, **kw_grid)

    b2_Spin = Spinbox(master, **kw_spin, textvariable=b2)
    b2_Spin.grid(row=1, column=3, **kw_grid)

    c2_Label = tk.Label(master, text="C2:")
    c2_Label.grid(row=1, column=4, **kw_grid)

    c2_Spin = Spinbox(master, **kw_spin, textvariable=c2)
    c2_Spin.grid(row=1, column=5, **kw_grid)

def main():
    root = tk.Tk()
    root.title("ShiftRight3 из ПЗ №5.2")

    a1, b1, c1, a2, b2, c2 = (tk.StringVar(root, 0) for _ in range(6))

    KeyArgs_grid = {
        "padx": 10,
        "pady": 10,
        "sticky": 'we'
    }
    checkCmd = (root.register(check), '%P')
    KeyArgs_spin = {
        "width": 10,
        "from_": -1000,
        "to": 1000,
        "increment": 1,
        "validate":'key',
        "validatecommand": checkCmd
    }
    
    first_nums(root, KeyArgs_grid, KeyArgs_spin)
    second_nums(root, KeyArgs_grid, KeyArgs_spin)

    Ready_button = tk.Button(root, text="Ready", command=start_shift)
    Ready_button.grid(row=2, column=2, columnspan=2, **KeyArgs_grid)

    try:
        root.mainloop()
    except KeyboardInterrupt:
        exit()
    


if __name__ == "__main__":
    main()