# File Name : Account.py
# Student Name: Jacob Farrell, Alisha Siddiqui, Hailey Manuel, William Claus
# Email: farrelcj@mail.uc.edu, Siddiqas@mail.uc.edu, manuelhv@mail.uc.edu, clausws@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 02/27/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Develop a simple banking system that manages customers, accounts, and transactions.
#
# Brief Description of what this module does: 
# This module defines the Account class, which handles bank account operations
# such as deposits, withdrawals, and balance checks.
#
# Citations: Stackoverflow
#
# Anything else that's relevant:
# - This module is a core part of the banking system and interacts with customers.

class Account:
    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owner = owner
        self._balance = balance
    
    def __str__(self):
        return f"Account({self.account_number}, Owner: {self.owner}, Balance: ${self._balance:.2f})"
    
    @property
    def balance(self):
        return self._balance
    
    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            raise ValueError("Balance cannot be negative")
    
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return f"Deposited ${amount:.2f}. New Balance: ${self._balance:.2f}"
        return "Deposit amount must be positive."
    
    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            return f"Withdrew ${amount:.2f}. Remaining Balance: ${self._balance:.2f}"
        return "Insufficient balance or invalid amount."

