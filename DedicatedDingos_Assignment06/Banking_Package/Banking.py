# File Name : Banking.py
# Student Name: Jacob Farrell, Alisha Siddiqui, Hailey Manuel, William Claus
# Email: farrelcj@mail.uc.edu, Siddiqas@mail.uc.edu, manuelhv@mail.uc.edu, clausws@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 02/27/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Develop a simple banking system that manages customers, accounts, and transactions.
#
# Brief Description of what this module does: 
# This module defines the Bank class, which manages multiple customers
# and allows listing all accounts within the bank.
#
# Citations: Stackoverflow
#
# Anything else that's relevant:
# - A bank can contain multiple customers, each with their own accounts

from Customer_Package.Customer import Customer
from Account_Package.Account import Account

class Banking:
    def __init__(self, name):
        self._name = name
        self.customers = []
    
    def __str__(self):
        return f"Banking({self._name}, Customers: {len(self.customers)})"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and value:
            self._name = value
        else:
            raise ValueError("Bank name must be a non-empty string")
    
    def add_customer(self, customer):
        if isinstance(customer, Customer):
            self.customers.append(customer)
            return f"Customer {customer.name} added to {self._name}."
        return "Invalid customer."
    
    def list_accounts(self):
        accounts = []
        for customer in self.customers:
            accounts.extend(customer.get_accounts())
        return accounts if accounts else "No accounts in the bank."
