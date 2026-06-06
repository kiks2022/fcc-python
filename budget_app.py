class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = self.name.center(30, '*') + '\n'
        items = ''
        for item in self.ledger:
            desc = item['description'][:23].ljust(23)
            amount = f"{item['amount']:.2f}".rjust(7)
            items += f"{desc}{amount}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

def create_spend_chart(categories):
    withdrawals = []
    for cat in categories:
        total = sum(-item['amount'] for item in cat.ledger if item['amount'] < 0)
        withdrawals.append(total)
    total_spent = sum(withdrawals)
    percentages = [int((w / total_spent) * 100) // 10 * 10 for w in withdrawals]
    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        line = str(i).rjust(3) + '|'
        for pct in percentages:
            line += ' o ' if pct >= i else '   '
        line += ' '
        chart += line + '\n'
    chart += '    ' + '-' * (len(categories) * 3 + 1) + '\n'
    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        line = '    '
        for cat in categories:
            if i < len(cat.name):
                line += ' ' + cat.name[i] + ' '
            else:
                line += '   '
        line += ' '
        chart += line
        if i < max_len - 1:
            chart += '\n'
    return chart

# Test Budget App
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food")

clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55, "jeans")

entertainment = Category("Entertainment")
entertainment.deposit(500, "initial deposit")
entertainment.withdraw(200, "concert tickets")

print(food)
print()
print(clothing)
print()
print(entertainment)
print()
print(create_spend_chart([food, clothing, entertainment]))
