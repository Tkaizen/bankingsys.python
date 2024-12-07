class BankAccount:
    def __init__(self, account_holder, account_balance=0):
        self.account_holder = account_holder
        self.account_balance = account_balance

    def deposit(self, amount):
        """Deposits money into the account"""
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited {amount}. New balance: {self.account_balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraws money from the account"""
        if amount > 0:
            if self.account_balance >= amount:
                self.account_balance -= amount
                print(f"Withdrew {amount}. New balance: {self.account_balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        """Checks the current balance of the account"""
        print(f"Current balance: {self.account_balance}")

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_holder):
        """Creates a new bank account"""
        if account_holder not in self.accounts:
            new_account = BankAccount(account_holder)
            self.accounts[account_holder] = new_account
            print(f"Account created for {account_holder}")
        else:
            print(f"Account already exists for {account_holder}")

    def get_account(self, account_holder):
        """Fetches an account for a specific account holder"""
        if account_holder in self.accounts:
            return self.accounts[account_holder]
        else:
            print(f"No account found for {account_holder}")
            return None

def main():
    bank = Bank()
    
    while True:
        print("\n--- Welcome to the Bank ---")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        
        choice = input("Please enter your choice: ")
        
        if choice == '1':
            name = input("Enter account holder's name: ")
            bank.create_account(name)
        elif choice == '2':
            name = input("Enter account holder's name: ")
            account = bank.get_account(name)
            if account:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
        elif choice == '3':
            name = input("Enter account holder's name: ")
            account = bank.get_account(name)
            if account:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
        elif choice == '4':
            name = input("Enter account holder's name: ")
            account = bank.get_account(name)
            if account:
                account.check_balance()
        elif choice == '5':
            print("Thank you for using the bank!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
