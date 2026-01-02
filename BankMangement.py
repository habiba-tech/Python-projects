class BankAccount:
    def __init__(self, acc_no, name, balance=0):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn")
        else:
            print("Insufficient balance")

    def show_details(self):
        print("\nAccount Number:", self.acc_no)
        print("Account Holder:", self.name)
        print("Balance:", self.balance)


class BankSystem:
    def __init__(self, filename="bank.txt"):
        self.accounts = {}
        self.filename = filename

    def create_account(self):
        acc_no = input("Enter Account Number: ")
        name = input("Enter Name: ")
        balance = float(input("Enter Initial Balance: "))

        self.accounts[acc_no] = BankAccount(acc_no, name, balance)
        print("Account created")

    def deposit_money(self):
        acc_no = input("Enter Account Number: ")
        if acc_no in self.accounts:
            amount = float(input("Enter Amount: "))
            self.accounts[acc_no].deposit(amount)
        else:
            print("Account not found")

    def withdraw_money(self):
        acc_no = input("Enter Account Number: ")
        if acc_no in self.accounts:
            amount = float(input("Enter Amount: "))
            self.accounts[acc_no].withdraw(amount)
        else:
            print("Account not found")

    def view_account(self):
        acc_no = input("Enter Account Number: ")
        if acc_no in self.accounts:
            self.accounts[acc_no].show_details()
        else:
            print("Account not found")

    def save_to_file(self):
        with open(self.filename, "w") as file:
            for acc in self.accounts.values():
                file.write(f"{acc.acc_no},{acc.name},{acc.balance}\n")
        print("Data saved to file")


# Main Program
bank = BankSystem()

while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. View Account")
    print("5. Save to File")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        bank.create_account()
    elif choice == "2":
        bank.deposit_money()
    elif choice == "3":
        bank.withdraw_money()
    elif choice == "4":
        bank.view_account()
    elif choice == "5":
        bank.save_to_file()
    elif choice == "6":
        print("Program Ended")
        break
    else:
        print("Invalid choice")
