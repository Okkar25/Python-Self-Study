class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance += amount
        print(f"\nDeposit complete. 📈")
        # print(f"\nDeposit complete. ${amount:.2f} deposited.")
        print(f"Amount ${amount} was deposited into account '{self.name}'.")
        self.getBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"Sorry, account '{self.name}' only has a balance of ${self.balance:.2f}. 💰"
            )

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw complete. 📉")
            print(f"Amount ${amount} was withdrawn from account '{self.name}'.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted ❌ : {error}")

    def transfer(self, amount, account):
        try:
            print("\n*************************************\n\nBeginning Transfer... 🔃")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)

            print(
                f"\nAccount '{account.name}' received ${amount} from account '{self.name}'"
            )
            print("\nTransfer Complete! ✅\n\n*************************************")
        except BalanceException as error:
            print(f"\nTransfer interrupted ❌ : {error}")


class InterestRewardsAccount(BankAccount):
    def deposit(self, amount):
        # self.balance += amount + (amount * 0.05)
        self.balance += amount * 1.05
        print(f"\nDeposit complete. 📈")
        print(f"Amount ${amount} was deposited into account '{self.name}'.")
        self.getBalance()


class SavingsAccount(InterestRewardsAccount):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.fee = 5  # pay every time withdrawn

    def withdraw(self, amount):
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= amount + self.fee
            print("\nWithdraw complete. 📉")
            print(f"Amount ${amount} was withdrawn from account '{self.name}'.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted ❌ : {error}")


