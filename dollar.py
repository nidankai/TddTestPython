class Dollar:
    amount = int()

    def __init__(self, amount):
        self.amount = amount

    def __eq__(self, other):
        if not isinstance(other, Dollar):
            return NotImplemented
        return self.amount == other.amount

    def times(self, multiplier):
        return Dollar(self.amount * multiplier)

    def equals(self, object):
        dollar = object
        return self.amount == dollar.amount
