import shutil

class ATMmachine:
    def __init__(self, cardNumber, pin, balance = 10000):
        self.cardNumber = cardNumber
        self.pin = pin
        self.balance = balance
    
    def checkBalance(self):

        print("Your Current Balance is: $", self.balance)

    def withdraw(self, withdrawal_amount):
        self.balance = self.balance - withdrawal_amount
        print('')
        print("You have successfully withdrawn $" + str(withdrawal_amount))
        print("Your current balance is now: $", self.balance)

    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        print('')
        print("You have successfully deposited $" + str(deposit_amount))
        print("Your current balance is now: $", self.balance)

    def changePin(self, new_pin):
      
        print("Your PIN has successfully been changed!")


def main():
    columns = shutil.get_terminal_size().columns
    print('')
    print("<< Welcome To Paradise Bank Corp. ATM >>".center(columns))
    print('')
    print('')
    card_number = input("Enter your card number: ")
    print('')
    pin_number = input("Enter your PIN number: ")
    print('')

    new_user = ATMmachine(card_number, pin_number)

    print("Choose your activity".center(columns))
    print("1.Balance Enquriy  2.Withdrawl  3.Deposit  4.Change PIN".center(columns))
    print('')
    activity = int(input("Enter Activity Number: "))
    print('')

    if (activity == 1):
        new_user.checkBalance()

    if (activity == 2):
        amount = int(input("Enter the amount: "))
        print('')
        new_user.withdraw(amount)

    if (activity == 3):
        amount = int(input("Enter the amount: "))
        print('')
        new_user.deposit(amount)

    if (activity == 4):
        new_pin = int(input("Enter the new PIN: "))
        print('')
        new_user.changePin(new_pin)

if __name__ == "__main__":
    main()

    

