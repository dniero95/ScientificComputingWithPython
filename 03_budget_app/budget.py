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
            amount_string = f'{float(transaction["amount"]):.2f}'
            amount_len = len(amount_string)


            description_len = len(transaction["description"])
            if description_len >= 23:
                text = transaction["description"][:23]
                description_len = 23
            else:
                text = transaction["description"]
            whitespace = 30 - description_len - amount_len

            description = f'{description}{text}{" "*whitespace}{amount_string}\n'
        return f'{self.name.center(30, "*")}\n{description}Total: {self.get_balance():.2f}'

    # representation of the obj
    def __repr__(self):
        return f'{self.__class__.__name__}({self.name})'

def create_spend_chart(categories:list)->str:
    # store the categories names in a list
    categories_names = [category.name for category in categories]

    # calculate the percentage
    withdraws = []
    for category in categories:
        total_withdraw = 0
        for transaction in category.ledger:
            withdraw = float(transaction["amount"])
            if withdraw < 0:
                total_withdraw += withdraw
        withdraws.append(total_withdraw)

    total = sum(withdraws)
    withdraws_percent = [int(abs((percent / total)*100)//10) for percent in withdraws]

    title = 'Percentage spent by category\n'
    percentages = ['100', ' 90', ' 80', ' 70', ' 60', ' 50' , ' 40', ' 30', ' 20', ' 10', '  0']
    y_axis = ''
    for index in range(len(percentages)):
        y_axis = f'{y_axis}{percentages[index]}|'
        for withdraw_percent in withdraws_percent:
            if int(percentages[index]) <= withdraw_percent * 10:
                y_axis = f'{y_axis} o '
        y_axis = f'{y_axis.rstrip()}\n'
    x_axis = f'{" "*4}{"-"*((len(categories_names)*3)+1)}\n'
    categories_description = ''
    index = 0
    while True:
        categories_description_line = f'{" "*5}'
        breakout = 0
        for name in categories_names:
            if index < len(name):
                categories_description_line = f'{categories_description_line}{name[index]}  '
            else:
                categories_description_line = f'{categories_description_line}   '
                breakout += 1
        categories_description = f'{categories_description}{categories_description_line.rstrip()}\n'
        index += 1
        if breakout == len(categories_names):
            break



    spend_chart_text = f'{title}{y_axis}{x_axis}{categories_description}'
    print(spend_chart_text)
