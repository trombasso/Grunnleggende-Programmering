annualInterestRate = float(input("Enter interest rate: "))
montlyIntrestRate = annualInterestRate / 1200

numberOfYears = int(input("Number of years: "))

loanAmount = float(input("How much is your loan: "))

monthlyPayment = loanAmount * montlyIntrestRate / (1 - 1 / (1 + montlyIntrestRate) ** (numberOfYears * 12))
totalPayment = (monthlyPayment * numberOfYears * 12)

print(f"Montly payments: {monthlyPayment:.2f}, Total payment: {totalPayment:.2f}")