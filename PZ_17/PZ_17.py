import tkinter as tk

def focus_next(event):
    event.widget.tk_focusNext().focus()
    return "break"

root = tk.Tk()
root.title("Registration Details")

uni_label = tk.Label(root, text="University:")
uni_label.grid(row=0, column=0, padx=10, pady=10)

uni_entry = tk.Entry(root)
uni_entry.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
uni_entry.bind("<Return>", focus_next)
uni_entry.focus() #Фокус в самом начале

inst_label = tk.Label(root, text="Institute:")
inst_label.grid(row=1, column=0, padx=10, pady=10)

inst_entry = tk.Entry(root)
inst_entry.grid(row=1, column=1, columnspan=3, padx=10, pady=10)
inst_entry.bind("<Return>", focus_next)

branch_label = tk.Label(root, text="Branch:")
branch_label.grid(row=2, column=0, padx=10, pady=10)

branch_combo = tk.ttk.Combobox(root)

root.mainloop()