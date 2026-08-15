class Transaction:
    def __init__(self, transaction_id, transaction_type, description, amount, category, date):

        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.description = description
        self.amount = amount
        self.category = category
        self.date = date

    def to_dict(self):
        return(
            "id": self.transaction_id,
            "type": self.transaction_type,
            "description": self.description,
            "amount": self.amount,
            "category": self.category,
            "date": str(self.date)
        )

    def __str__(self):
        return (
            f"Id: {self.transaction_id} | "
            f"Type: {self.transaction_type} | "
            f"Description: {self.description} | "
            f"Amount: {self.amount} | "
            f"Category: {self.category} | "
            f"Date: {self.date} | "
        )
import json
from datetime import date
class FinanaceManager:
    def __init__(self, filename="finance.json"):
        self.filename = filename
        self.transactions = []

    def get_next_id(self):
        if not self.transactions:
            return 1
        return max(transaction.transaction_id for transaction in self.transactions)+1

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def add_income(self):
        description = input("Description: ").strip()
        if not description:
            print("Description cannot be empty")
            return
        try:
            amount = float(input("Amount: "))
        except ValueError:
            print("invalid amount")
            return
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
        category = input("Category").strip()
        if not category:
            print("category cannot empty")
            return
        transaction = Transaction(
            self.get_next_id(),
            "income",
            description,
            amount,
            category,
            date.today()
        )
        self.add_transaction(transaction)
        print("Income successfully")

    def add_expense(self):
        description = input("Description: ").strip().lower()
        if not description:
            print("description cannot be empty")
            return
        try:
            amount = float(input("Amount: "))
        except ValueError:
            print("Invalid amount!")
            return
        if amount <= 0:
            print("Amount must be greater than 0.")
            return
        category = input("Category: ").strip()
        if not category:
            print("category cannot be empty")
            return
        transaction = Transaction(
            self.get_next_id(),
            "expense",
            description,
            amount,
            category,
            date.today()
        )
        self.add_transaction(transaction)
        print("Expense added successfully")

    def remove_transaction(self, index):
        try:
            index = int(index) -1
        except ValueError:
            print("Invalid index!")
            return
        if 0 <= index < len(self.transactions):
            removed = self.transactions.pop(index)
            print(f"{removed.description} deleted")
        else:
            print("Number not found")

    def search_transaction(self):
        search_term = input("Description or Category: ").strip()
        if not search_term:
            print("search_term cannot be empty")
            return
        found = False

        for transaction in self.transactions:
            if search_term.lower() in transaction.description.lower():
                print(transaction)
                found = True

            elif search_term.lower() in transaction.category.lower():
                print(transaction)
                found = True
        if not found:
            print("Transaction not found")

    def show_transactions(self):
        if not self.transactions:
            print("no transaction")
            return

        print("Transactions: ")
        for i, transaction in enumerate(self.transactions, start=1):
            print(f"{i}. {transaction}")

    def calculate_balance(self):
        balance = 0
        for transaction in self.transactions:
            if transaction.type == "income":
                balance += transaction.amount
            elif transaction.type == "expense":
                balance -= transaction.amount
        return balance

    def total_income(self):
        total = 0
        for transaction in self.transactions:
            if transaction.type == "income":
                total += transaction.amount
        return total

