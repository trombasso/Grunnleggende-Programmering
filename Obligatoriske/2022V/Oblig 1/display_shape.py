from ast import Delete
import tkinter as tk
from tkinter import ttk


class Shapes:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Display Shapes")
        self.root.geometry("300x200")
        self.root.resizable(False, False)
        # self.root.configure(bg="gray")

        self.selection = tk.StringVar()
        self.select_shape = ttk.Combobox(self.root, textvariable=self.selection)
        self.select_shape["values"] = ["Rectangle", "Oval", "Arc"]
        self.select_shape["state"] = "readonly"
        self.select_shape.grid(column=0, row=0)
        self.select_shape.bind("<<ComboboxSelected>>", self.shapechange)

        self.shape = tk.Canvas(self.root)
        self.shape.grid(column=0, row=1)

        self.root.mainloop()

    def shapechange(self, *args):
        if self.select_shape.get() == "Rectangle":
            print(self.select_shape.get())
            # self.shape.delete("all")
            self.shape = tk.Canvas(self.root)
            self.shape.create_rectangle(10, 50, 290, 60, outline="#000000", fill=None)
            self.shape.grid(column=0, row=1)
        elif self.select_shape.get() == "Oval":
            print(self.select_shape.get())
            # self.shape.delete("all")
            self.shape = tk.Canvas(self.root)
            self.shape.create_oval(50, 30, 220, 20, outline="#0000FF", fill="red")
            self.shape.grid(column=0, row=1)
        else:
            # self.shape.delete()
            print(self.select_shape.get())


def main():
    Shapes()


if __name__ == "__main__":
    main()
