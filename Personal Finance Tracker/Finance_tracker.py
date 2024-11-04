import json
import os
from collections import defaultdict

class TransactionError(Exception):
    """Custom exception for transaction errors."""
    pass

class FinanceTracker:
    def __init__(self, filename='data.json'):
        self.filename = filename
        self.transactions = self.load_data()
        self.category_summary = defaultdict(float)
        
    def load_data(self):
        """Load transaction data from the JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as file:
                    data = file.read().strip()
                    return json.loads(data) if data else []
            except (json.JSONDecodeError, ValueError) as e:
                print(f"Error loading data: {e}")
                return []  # Return an empty list if the file is corrupted or empty
        return []  # Return an empty list if the file does not exist



    
    def save_data(self):
        """Save transaction data to the JSON file."""
        with open(self.filename, 'w') as file: 
            json.dump(self.transactions, file, indent=4)

    

    def log_transaction(func):
        """Decorator to log transactions."""
        def wrapper(self, *args, **kwargs):
            print(f"Decorator called with args: {args}, kwargs: {kwargs}") 
            result = func(self, *args, **kwargs)
            print(f"Transaction logged: {args[0]} {kwargs.get('category', 'N/A')} as {kwargs.get('transaction_type', 'N/A')}")
            return result
        return wrapper


    @log_transaction
    def add_transaction(self, amount, category, transaction_type):
        """Add a new transaction."""
        transaction = {
            'Amount' : amount,
            'Category' : category,
            'Type' : transaction_type
        }
        self.transactions.append(transaction)
        self.category_summary[category] += amount if transaction_type == 'income' else -amount
        self.save_data()
    
    def get_transactions(self):
        """Generating to Yield transactions."""
        for transaction in self.transactions:
            yield transaction
    def display_summary(self):
        """Display Category Summary."""
        print("Category Summary:")
        for category, total in self.category_summary.items():
            print(f"{category}: {total}")
