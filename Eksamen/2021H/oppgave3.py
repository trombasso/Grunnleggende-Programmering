import tkinter as tk


class Calculator:
    def __init__(self, log=[]):
        self.log = log

    def calculate(self, operand1, operand2, operator):  # eval, returnres, put into log
        self.operand1 = operand1
        self.operand2 = operand2
        self.operator = operator

        if operator == "*":
            self.log.append(f"{str(operand1)} {operator} {str(operand2)} = {operand1 * operand2}")
            return operand1 * operand2
        elif operator == "/":
            self.log.append(f"{str(operand1)} {operator} {str(operand2)} = {operand1 / operand2}")
            return operand1 * operand2
        elif operator == "+":
            self.log.append(f"{str(operand1)} {operator} {str(operand2)} = {operand1 + operand2}")
            return operand1 * operand2
        elif operator == "-":
            self.log.append(f"{str(operand1)} {operator} {str(operand2)} = {operand1 - operand2}")
            return operand1 * operand2

    def get_log(self):
        return self.log

    def get_last_logged(self):
        if len(self.log) > 0:
            last_logged = self.log[len(self.log) - 1 :]
        return last_logged

    def clear_log(self):
        self.log = []


def calculateGUI(*args):
    operand1_local = operand1.get()
    operand2_local = operand2.get()
    operator_local = operator.get()
    value = calc.calculate(operand1_local, operand2_local, operator_local)
    result.set(value)
    from_log = calc.get_log()
    log.set(from_log)


def clear():
    calc.clear_log()


def quit():
    exit()


if __name__ == "__main__":

    calc = Calculator()

    window = tk.Tk()
    window.title("Calculator")

    frame = tk.Frame(window)
    frame.pack()

    tk.Label(frame, text="Operand1").grid(column=0, row=0)
    operand1 = tk.IntVar(frame, value=0)
    tk.Entry(frame, width=10, textvariable=operand1).grid(column=1, row=0)

    tk.Label(frame, text="Operator (+ - * /)").grid(column=0, row=1)
    operator = tk.StringVar(frame, value="")
    tk.Entry(frame, width=4, textvariable=operator).grid(column=1, row=1)

    tk.Label(frame, text="Operand2").grid(column=0, row=2)
    operand2 = tk.IntVar(frame, value=0)
    tk.Entry(frame, width=10, textvariable=operand2).grid(column=1, row=2)

    tk.Label(frame, text="Result").grid(column=0, row=3)
    result = tk.IntVar(frame)
    result_print = tk.Label(frame, textvariable=result).grid(column=1, row=3)

    buttonframe = tk.Frame(window)  # buttons
    buttonframe.pack()
    tk.Button(buttonframe, text="Calculate", command=lambda: calculateGUI(operand1, operand2, operator)).grid(column=0, row=0)
    tk.Button(buttonframe, text="Clear Log", command=clear).grid(column=1, row=0)
    tk.Button(buttonframe, text="Quit", command=quit).grid(column=2, row=0)

    log = tk.StringVar(buttonframe, value=calc.get_log())
    log = tk.Text(buttonframe, width=33, height=10).grid(columnspan=3, column=0, row=1)

    window.mainloop()
