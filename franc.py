class Franc:
    _amount = int()

    def __init__(self, amount):
        self._amount = amount

    def __eq__(self, other):
        if not isinstance(other, Franc):
            return NotImplemented
        return self._amount == other._amount

    def times(self, multiplier):
        return Franc(self._amount * multiplier)

    def equals(self, object):
        Franc = object
        return self._amount == Franc._amount
