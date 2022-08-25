class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ''):
        self.ledger.append(
            {
                "amount": amount,
                "description": description
            })

    def withdraw(self, amount, description = ''):
        self.ledger.append(
            {
                "amount": - amount,
                "description": description
            })

    def get_balance(self):
        balance = 0
        for transaction in self.ledger:
            balance += transaction['amount']
        return balance

    def transfer(self):
        pass



# def create_spend_chart(categories):