class Category:
    def __init__(self, name: str):
        self.name = name
        # instance variable ledger
        self.ledger = []

    # add amount and description to ledger list
    def deposit(self, amount: float, description=''):
        self.ledger.append(
            {
                "amount": amount,
                "description": description
            })

    # take an amount from the obj
    def withdraw(self, amount: float, description='') -> bool:

        if self.check_funds(amount):
            self.ledger.append(
                {
                    "amount": -amount,
                    "description": description
                })
            return True

        return False

    # get the total balance of a category obj
    def get_balance(self) -> float:
        balance = .0
        for transaction in self.ledger:
            balance += transaction['amount']
        return balance

    # transfer an amount form a category obj to another category obj
    def transfer(self, amount: float, category: object) -> bool:
        check = self.check_funds(amount)
        if check:
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return check
        return check

    # check if the total found are more or less than a given amount
    def check_funds(self, amount: float) -> bool:
        if self.get_balance() < amount:
            return False
        return True

    # string version of the obj

    def __str__(self):
        description = f''
        for transaction in self.ledger:
            amount_len = len(str(transaction["description"]))
            if len(transaction["description"]) >= 23:
                text = transaction["description"][:23]
            else:
                text = transaction["description"]
            text_len = len(text)
            description = f'{description}\n{text}{" " * (30 - (text_len + amount_len + 3))}{float(transaction["amount"]):f.2}'
        return f'{self.name.center(30, "*")}\n{description}'

    # representation of the obj

    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'

# def create_spend_chart(categories):
