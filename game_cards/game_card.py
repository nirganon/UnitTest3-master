
class Card:
    def __init__(self, value: int, suit: int):
        self.value= value
        self.suit= suit

    def __gt__(self, other):
        if self.value == 1:
            self.value = 14
        if self.value > other.value:
            return True
        if self.value < other.value:
            return False
        if self.value == other.value:
            if self.suit > other.suit:
                return True
            else:
                return False