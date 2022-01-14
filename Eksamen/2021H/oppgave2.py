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


def main():
    calculator = Calculator()
    calculator.calculate(1, 2, "+")
    calculator.calculate(2, 2, "*")
    calculator.calculate(16, 2, "/")
    print(calculator.get_log())
    print(calculator.get_last_logged())


if __name__ == "__main__":
    main()
