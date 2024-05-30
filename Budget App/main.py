class Category:
    # Initialize the new category with a name and a ledger
    def __init__(self, name):
        self.name = name
        self.ledger = []

    # Return the full ledger with category name, transactions, and the balance after all transactions
    def __str__(self):
        ledger = ''
        # Add title
        no_of_asterisks = (30 - len(self.name)) // 2
        title = f"{'*' * no_of_asterisks}{self.name}{'*' * no_of_asterisks}"
        if len(title) != 30:
            title += '*'
        ledger += title + '\n'
        # Add transactions
        for trans in self.ledger:
            money = str(float(trans['amount']))
            if len(money[money.find('.')+1:]) == 1:
                money += '0'
            ledger += f"{trans['description'][:23].ljust(23)}{money.rjust(7)}\n" 
        # Add balance
        ledger += f'Total: {self.get_balance()}'
        # return entire ledger
        return ledger

    # Deposit money into the category, with a description of the transaction
    def deposit(self, amount, description=''):
        self.ledger.append({"amount": round(amount, 2), "description": description})

    # Withdraw money from the category, with a description of the transaction; opposite of deposit
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.deposit(-amount, description)
            return True
        return False

    # Transfer money from one category to another and save the transaction to both ledgers
    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    # Return the balance of the category
    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction["amount"]
        return round(balance, 2)

    # Return true if the balance is greater than the amount; To use with withdraw and transfer
    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        return True

# Return a bar graph of the percent of total expenses for each category.
def create_spend_chart(categories):
    # For creating the graph
    spend_chart = []

    # Add title
    spend_chart += 'Percentage spent by category\n'

    # Find the total/sum of expenses (withdrawals).
    total = 0
    for category in categories:
        category.total_spent = 0
        for transaction in category.ledger:
            if transaction['amount'] < 0:
                total -= transaction['amount']
                category.total_spent -= transaction['amount']
    # Find the percent of the total expenses for each category
    for category in categories:
        category.percent_of_total = int((category.total_spent / total) * 100)

    # Match each percent to a range of multiples of 10; If the percent for [category] is more than the multiple, fit the percent into the range. e.g: 65% -> 0-60%
    graph_rows = [[num] for num in range(100, -1, -10)]
    for category in categories:
        for row in graph_rows:
            if category.percent_of_total >= row[0]:
                row.append('o') # Use 'o' as character for the bars
            else:
                row.append(' ')
    # Add the percentages and bars
    for row in graph_rows:
        spend_chart += f"{str(row[0]).rjust(3)}| {'  '.join(row[1:])}"
        spend_chart += '  \n'
    # Add separator
    spend_chart += '    '
    spend_chart += f"{'-' * len(categories) * 3}-"

    # Add the names of each category in the graph
    max_name_length = max([len(category.name) for category in categories])
    char_rows = [[] for _ in range(max_name_length)]
    for name in [category.name.ljust(max_name_length) for category in categories]:
        for index, row in enumerate(char_rows):
            row.append(name[index]) 
    for row in char_rows:
            spend_chart += '\n     '
            spend_chart += f"{'  '.join(row[index] for index in range(len(row)))}"
            spend_chart += '  '
    # Return entire bar graph
    return ''.join(spend_chart)


# For testing
food = Category("Food") # Create category for food
entertainment = Category("Entertainment") # Create category for entertainent
business = Category("Business") # Create category for business
food.deposit(900, "deposit") # Deposit $900
entertainment.deposit(900, "deposit") # Deposit $900
business.deposit(900, "deposit") # Deposit $900
food.withdraw(105.55, "mcdonalds") # Withdraw $105.55
entertainment.withdraw(33.40, "avengers") # Withdraw $33.40
business.withdraw(10.99, "dinner") # Withdraw $10.99
education = Category("Education") # Create category for education
entertainment.transfer(400, education) # Transfer $400 to education
education.withdraw(150, "books") # Withdraw $150
# Print the ledger for each category
print(food, '\n')
print(entertainment, '\n')
print(business, '\n')
print(education, '\n')
# Print the bar graph of the percent of total expenses for each category.
print(create_spend_chart([business, food, entertainment, education])) 

"""
Note: There are many seemingly random inclusions of whitespace throughtout the strings within {create_spend_chart}, such as whitespace before newline sequences. This is to perfectly match the graph with the formatting of the answer checker, because its requirements are highly strict, albeit very vague. 
"""
