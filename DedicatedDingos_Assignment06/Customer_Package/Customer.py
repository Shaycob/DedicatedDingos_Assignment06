# File Name : Customer.py
# Student Name: Jacob Farrell, Alisha Siddiqui, Hailey Manuel, William Claus
# Email: farrelcj@mail.uc.edu, Siddiqas@mail.uc.edu, manuelhv@mail.uc.edu, clausws@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 02/27/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Develop a simple banking system that manages customers, accounts, and transactions.
# Brief Description of what this module does: This module defines the Customer class, which allows users to create accounts,
# manage their accounts, and view their balances.
# Citations: Stackoverflow
# Anything else that's relevant:Each customer can have multiple accounts.

from Account import Account

class Customer:
    def __init__(self, name, customer_id):
        self._name = name
        self.customer_id = customer_id
        self.accounts = []
    
    def __str__(self):
        return f"Customer({self.customer_id}, Name: {self._name}, Accounts: {len(self.accounts)})"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and value:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")
    
    def open_account(self, account_number, initial_deposit=0.0):
        new_account = Account(account_number, self._name, initial_deposit)
        self.accounts.append(new_account)
        return f"Account {account_number} opened with balance ${initial_deposit:.2f}"
    
    def get_accounts(self):
        return [str(acc) for acc in self.accounts]

