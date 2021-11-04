import tkinter as tk


def calculate(*args):
    try:
        value = float(celcius.get())
        fahrenheit.set(float(value * 1.8 + 32))
    except ValueError:
        pass


root = tk.Tk()
root.title("Celcius to Fahrenheit")

mainframe = tk.Frame(root)
mainframe.grid(column=0, row=0)
# root.columnconfigure(0, weight=1)
# root.rowconfigure(0, weight=1)

celcius = tk.StringVar()
celcius_entry = tk.Entry(mainframe, width=7, textvariable=celcius)
celcius_entry.grid(column=2, row=1)

fahrenheit = tk.StringVar()
tk.Label(mainframe, textvariable=fahrenheit).grid(column=2, row=2)
tk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3)
tk.Label(mainframe, text="Celcius").grid(column=3, row=1)
tk.Label(mainframe, text="is equivalent to").grid(column=1, row=2)
tk.Label(mainframe, text="fahrenheit").grid(column=3, row=2)

for child in mainframe.winfo_children():
    child.grid_configure()  # padx=5, pady=5)

celcius_entry.focus()
root.bind("<Return>", calculate)

root.mainloop()
