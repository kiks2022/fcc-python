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
    # Calculate withdrawals per category
    withdrawals = []
    for cat in categories:
        total = sum(-item['amount'] for item in cat.ledger if item['amount'] < 0)
        withdrawals.append(total)

    total_spent = sum(withdrawals)

    # Calculate percentages rounded down to nearest 10
    percentages = [int((w / total_spent) * 100) // 10 * 10 for w in withdrawals]

    # Build chart
    chart = "Percentage spent by category\n"

    for i in range(100, -1, -10):
        line = str(i).rjust(3) + '|'
        for pct in percentages:
            line += ' o ' if pct >= i else '   '
        line += ' '
        chart += line + '\n'

    # Horizontal line
    chart += '    ' + '-' * (len(categories) * 3 + 1) + '\n'

    # Category names vertically
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
