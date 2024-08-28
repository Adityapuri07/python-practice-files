class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount}. Current balance is ${self.balance}."
        else:
            return "Deposit amount must be greater than zero."

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f"Withdrawn ${amount}. Current balance is ${self.balance}."
            else:
                return "Insufficient balance."
        else:
            return "Withdraw amount must be greater than zero."


def main():
    atm = ATM(1000)  # Initialize ATM with $1000 balance

    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print("Current Balance:", atm.check_balance())
        elif choice == '2':
            amount = float(input("Enter deposit amount: $"))
            print(atm.deposit(amount))
        elif choice == '3':
            amount = float(input("Enter withdrawal amount: $"))
            print(atm.withdraw(amount))
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
