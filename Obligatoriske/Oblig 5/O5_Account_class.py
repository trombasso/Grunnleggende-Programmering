class Account:
    def __init__(self, id=0, balance=100, annual_interest_rate=0):
        self.__id = int(id)
        self.__balance = float(balance)
        self.__annual_interest_rate = float(annual_interest_rate)

    @property
    def id(self):
        return self.__id

    @property
    def balance(self):
        return self.__balance

    @property
    def annual_interest_rate(self):
        return self.__annual_interest_rate

    @id.setter
    def id(self, value):
        self.__id = value

    @balance.setter
    def balance(self, value):
        self.__balance = value

    @annual_interest_rate.setter
    def annual_interest_rate(self, value):
        self.__annual_interest_rate = value

    def get_monthly_interest_rate(self):
        monthly_interest_rate = self.annual_interest_rate / 12
        return monthly_interest_rate

    def get_monthly_interest(self):
        return self.balance * self.get_monthly_interest_rate()

    def withdraw(self, value):
        self.balance -= value

    def deposit(self, value):
        self.balance += value


"""
Use this formula to calculate the monthly interest: balance * monthly_interestRate.

monthly_interestRate is annual_interestRate/12, 
Note that annualInterestRate is a percent (like 4.5%). You need to divide it by 100.)

Write a test program that creates an Account object with an account id of 1122, 
a balance of $20,000, and an annual interest rate of 4.5%. Use the withdraw method 
to withdraw $2,500, use the deposit method to deposit $3,000, and print the id, balance, m
onthly interest rate, and monthly interest.



"""


def main():

    konto1 = Account()
    konto1.id(1122)
    konto1.balance(20000)
    konto1.annual_interest_rate(4.5)

    konto1.whitdraw(2500)
    konto1.deposit(3000)
    print(
        f"konto id {konto1.id()}, Monthly Interest Rate/interest: {konto1.get_monthly_interest_rate()}, \
        {konto1.get_monthly_interest()}"
    )

    """
    create account, 
    id 1122
    balance $20.000,-
    annual interest rate 4,5
    
    withdraw $3.000,-
    print id, balance, monthly interest rate and monthly interest.
    """

    pass


if __name__ == "__main__":
    main()
