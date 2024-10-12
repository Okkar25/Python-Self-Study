from bank_accounts import *


# Function to handle user input
def main():
    accounts = {}

    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transfer")
        print("5. View Balance")
        print("6. View Available Accounts")
        print("7. Delete Account")
        print("8. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            # Creating a new account
            acct_type = input("Enter account type (basic/rewards/savings): ").lower()
            name = input("Enter account name: ")
            initialAmount = float(input("Enter initial balance: "))

            if acct_type == "basic":
                accounts[name] = BankAccount(initialAmount, name)
            elif acct_type == "rewards":
                accounts[name] = InterestRewardsAccount(initialAmount, name)
            elif acct_type == "savings":
                accounts[name] = SavingsAccount(initialAmount, name)
            else:
                print("Invalid account type!")

        elif choice == "2":
            # Depositing money
            name = input("Enter account name: ")
            if name in accounts:
                amount = float(input("Enter amount to deposit: "))
                accounts[name].deposit(amount)
            else:
                print("Account not found!")

        elif choice == "3":
            # Withdrawing money
            name = input("Enter account name: ")
            if name in accounts:
                amount = float(input("Enter amount to withdraw: "))
                accounts[name].withdraw(amount)
            else:
                print("Account not found!")

        elif choice == "4":
            # Transferring money
            from_acct = input("Enter the name of the account to transfer from: ")
            to_acct = input("Enter the name of the account to transfer to: ")
            if from_acct in accounts and to_acct in accounts:
                amount = float(input("Enter amount to transfer: "))
                accounts[from_acct].transfer(amount, accounts[to_acct])
            else:
                print("One or both accounts not found!")

        elif choice == "5":
            # Viewing balance
            name = input("Enter account name: ")
            if name in accounts:
                accounts[name].getBalance()
            else:
                print("Account not found!")

        elif choice == "6":
            # Viewing available accounts
            if accounts:
                print("\nAvailable Accounts:")
                for account_name in accounts:
                    print(f" - {account_name}")
            else:
                print("No accounts available!")

        elif choice == "7":
            # Deleting an account
            name = input("Enter the account name to delete: ")
            if name in accounts:
                confirm = input(
                    f"Are you sure you want to delete the account '{name}'? (yes/no): "
                )
                if confirm.lower() == "yes":
                    del accounts[name]
                    print(f"\nAccount '{name}' has been deleted. 🗑️")
                else:
                    print(f"Account '{name}' deletion canceled.")
            else:
                print("Account not found!")

        elif choice == "8":
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid option! Please try again.")


# Run the program
if __name__ == "__main__":
    main()
