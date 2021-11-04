import tkinter as tk

win = tk.Tk()  # Create a tkinter master frame
win.title("Fahrenheit to Celcius Converter")
win.geometry("450x150")  # Set the size of the window
win.resizable(False, False)  # Make the window size fixed

mainframe = tk.Frame(win)
mainframe.pack()

header = tk.Label(mainframe, text="Celcius to Fahrenheit")
inpt = tk.Entry(mainframe, width=20)
button = tk.Button(mainframe, text="Convert")
output = tk.Label(mainframe, text="Test")

header.grid(row=0, column=0, columnspan=3)
inpt.grid(row=1, column=0)
button.grid(row=1, column=1)
output.grid(row=1, column=2)


win.mainloop()
