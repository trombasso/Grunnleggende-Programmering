import tkinter as tk
from tkinter import ttk


class Shapes:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Display Shapes")
        self.root.geometry("300x200")
        self.root.resizable(False, False)

        self.selection = tk.StringVar()
        self.select_shape = ttk.Combobox(self.root, textvariable=self.selection, justify="center")
        self.select_shape["values"] = ["--- Select Shape ---", "Rectangle", "Oval", "Arc"]
        self.select_shape["state"] = "readonly"
        self.select_shape.current(0)
        self.select_shape.grid(column=0, row=0)
        self.select_shape.bind("<<ComboboxSelected>>", self.shapechange)

        self.shape = tk.Canvas(self.root)
        self.shape.grid(column=0, row=1)

        self.root.mainloop()

    def shapechange(self, *args):
        if self.select_shape.get() == "Rectangle":
            self.shape = tk.Canvas(self.root)
            self.shape.create_rectangle(10, 10, 285, 160, outline="#000000", fill=None)
            self.shape.grid(column=0, row=1)
        elif self.select_shape.get() == "Oval":
            self.shape = tk.Canvas(self.root)
            self.shape.create_oval(10, 10, 285, 160, outline="#000000", fill="red")
            self.shape.grid(column=0, row=1)
        elif self.select_shape.get() == "Arc":
            self.shape = tk.Canvas(self.root)
            self.shape.create_arc(10, 10, 285, 160, outline="#000000", fill="red", width=3)
            self.shape.grid(column=0, row=1)
        else:
            self.shape = tk.Canvas(self.root)
            self.shape.grid(column=0, row=1)


if __name__ == "__main__":
    Shapes()
