class Dollar:
    amount = int()

    def __init__(self, amount):
        self.amount = amount

    def times(self, multiplier):
        self.amount *= multiplier
