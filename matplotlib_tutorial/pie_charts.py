import matplotlib.pyplot as plt

# Data
categories = [
    'Rent', 'Groceries', 'Utilities', 'Internet and Cable',
    'Transportation', 'Entertainment', 'Insurance',
    'Savings', 'Miscellaneous'
]

expenses = [1200, 450, 150, 100, 200, 150, 300, 400, 50]
# expenses.sort()
# pie() function to draw pie charts:

explode = [0.2, 0, 0, 0, 0, 0, 0, 0, 0]

plt.figure(figsize=(9, 7))
plt.title('Monthly Household Expenses')
plt.pie(expenses, labels=categories,
        startangle=90, explode=explode, autopct='%1.1f%%'
        )

plt.legend(title='Categories')
plt.tight_layout()
plt.show()
