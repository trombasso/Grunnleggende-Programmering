import tkinter as tk
from tkinter import ttk


class Shapes:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Movable Vertices")
        self.root.geometry("600x400")
        self.root.resizable(True, True)

        self.root.mainloop()


if __name__ == "__main__":
    Shapes()
