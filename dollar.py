class Dollar:
    _amount = int()

    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        if not isinstance(other, Dollar):
            return NotImplemented
        return self._amount == other._amount

    def times(self, multiplier):
        return Dollar(self._amount * multiplier)

    def equals(self, object):
        dollar = object
        return self._amount == dollar.amount
