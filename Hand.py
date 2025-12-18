import random
class Hand:
    def __init__(self, cards):
        self.cards = cards
    def add_card(self, card):
        self.cards.append(card)
    def remove_card(self, card):
        self.cards.remove(card)
    def calculate_value(self):
        value = 0
        for card in self.cards:
            if card.value == "K":
                value += 13
            else:
                value += int(card.value)
        return value
    def print_cards(self):
        n_cards = len(self.cards)
        for i in range(n_cards):
            print(f" ___", end="\t")
        print()
        for i in range(n_cards):
            if self.cards[i].value == "10":
                print(f"|{self.cards[i].value} |", end="\t")
            else:
                print(f"|{self.cards[i].value}  |", end="\t")
        print()
        for i in range(n_cards):
            print(f"| {self.cards[i].suit} |", end="\t")
        print()
        for i in range(n_cards):
            if self.cards[i].value == "10":
                print(f"|{self.cards[i].value}_|", end="\t")
            else:
                print(f"|{self.cards[i].value}__|", end="\t")
        print()

class Deck(Hand):
    def __init__(self, cards):
        super().__init__(cards)

    def mix_cards(self):
        random.shuffle(self.cards)
    def deal_hand(self, n):
        print("x")




