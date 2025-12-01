# ♤, ♡, ♢, ♧
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def get_value(self):
        return self.value
    def show_card(self):
        if (self.value == "10"):
            print("_"*5)
            print(f"|{self.value} |")
            print(f"| {self.suit} |")
            print(f"|_{self.value}|")
        else:
            print("_" * 5)
            print(f"|{self.value}  |")
            print(f"| {self.suit} |")
            print(f"|__{self.value}|")