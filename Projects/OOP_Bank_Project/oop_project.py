from bank_accounts import *

Okkar = BankAccount(1000, "Okkar")
Novak = BankAccount(2000, "Novak")

Okkar.getBalance()
Novak.getBalance()

Okkar.deposit(3000)
Novak.deposit(500)

Okkar.withdraw(2500)
Novak.withdraw(500)

Novak.transfer(10000, Okkar)
Novak.transfer(1000, Okkar)

Jim = InterestRewardsAccount(1000, "Jim")
Jim.getBalance()
Jim.deposit(100)
Jim.transfer(100, Novak)

Blaze = SavingsAccount(5000, "Blaze")
Blaze.getBalance()
Blaze.deposit(1000)
Blaze.transfer(10000, Novak)
Blaze.transfer(1000, Novak)
