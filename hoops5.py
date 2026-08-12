# Abstraction
# Problem: ATM Withdrawal

from abc import ABC, abstractmethod


class ATM(ABC):

    @abstractmethod
    def withdraw(self):
        pass


class BankATM(ATM):

    def withdraw(self):
        amount = int(input("Enter withdrawal amount: "))
        print("Withdrawn Amount:", amount)
        print("Transaction Successful")


atm = BankATM()
atm.withdraw()