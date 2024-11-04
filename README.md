This is my third mini project with python.

Personal Finance Tracker
Overview:
The Personal Finance Tracker is a simple yet powerful tool designed to help users manage their finances effectively. This Python application allows users to log transactions, categorize them as income or expenses, and view a summary of their financial activities. With a focus on usability and data persistence, this tracker is an ideal solution for anyone looking to keep their finances organized.

Features:
1)Add Transactions: Users can easily log new transactions by specifying the amount, category, and whether it is an income or expense.
2)View Transactions: All logged transactions can be viewed in a straightforward list format, making it easy to track financial activity.
3)Display Summary: Users can view a summary of their financial data categorized by income and expenses, providing insights into spending habits.
4)Data Persistence: Transactions are stored in a JSON file (data.json), ensuring that data is saved between sessions and can be accessed later.
5)Error Handling: Custom exceptions handle potential errors during transaction logging, ensuring a smooth user experience

Usage:
1)Launch the application and follow the prompts.
2)Select options to add transactions, view all transactions, or display a summary of your finances.
3)Use the application continuously to keep track of your financial activities.

Example Data
[
    {
        "Amount": 80000.0,
        "Category": "client payment",
        "Type": "income"
    },
    {
        "Amount": 25000.0,
        "Category": "pay bills (electric, Wifi, service-charge)",
        "Type": "expense"
    }
]
