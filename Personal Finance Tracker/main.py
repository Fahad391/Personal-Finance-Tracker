from Finance_tracker import FinanceTracker, TransactionError

def main():
    tracker = FinanceTracker()

   
    while True:
        print("Welcome to the Personal Finance Tracker")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Display Summary")
        print("4. Exit")

        choice = input("Select your option: ")

        if choice == '1':
            try:
                amount = float(input("Enter the amount: "))
                category = input("Enter the category: ")
                transaction_type = input("Enter 'income' or 'expense': ")
                tracker.add_transaction(amount, category=category, transaction_type=transaction_type)  
                print("Transaction added!")

            except TransactionError as e:
                print(f"Error : {e}")               

        elif choice == '2':
          print("Transactions:")
          for transaction in tracker.get_transactions():
              print(transaction)
        
        elif choice == '3':
            tracker.display_summary()
        
        elif choice == '4':
            break

if __name__ == '__main__':
    main()
