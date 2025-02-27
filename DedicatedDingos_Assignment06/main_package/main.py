# File Name : main.py
# Student Name: Jacob Farrell, Alisha Siddiqui, Hailey Manuel, William Claus
# Email: farrelcj@mail.uc.edu, Siddiqas@mail.uc.edu, manuelhv@mail.uc.edu, clausws@mail.uc.edu
# Assignment Number: Assignment 06
# Due Date: 02/27/2025
# Course #/Section: IS4010-001
# Semester/Year: Spring 2025
# Brief Description of the assignment: Develop a simple banking system that manages customers, accounts, and transactions.
#
# Brief Description of what this module does: 
# This module initializes the banking system by creating a bank, adding customers,
# opening accounts, and listing all accounts in the system.
#
# Citations: Stackoverflow
#
# Anything else that's relevant:
# - This is the entry point for running the banking system.

from Customer_Package.Customer import Customer
from Banking_Package.Banking import Banking
from Account_Package.Account import Account

def main():
    # Creating a bank
    bank = Banking("Global Bank")
    
    # Creating a customer
    customer = Customer("John Doe", "C123")
    print(bank.add_customer(customer))
    
    # Customer opens an account
    print(customer.open_account("A1001", 500.00))
    
    # Viewing bank accounts
    print("Bank Accounts:", bank.list_accounts())
    
if __name__ == "__main__":
    main()