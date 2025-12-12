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
            value += card.value
    def print_cards(self):
        n_cards = len(self.cards)
        for i in range(n_cards):
            print(f" ___", end="\t")
        print()
        for i in range(n_cards):
            print(f"|{self.cards[i].value}  |", end="\t")
        print()
        for i in range(n_cards):
            print(f"| {self.cards[i].suit} |", end="\t")
        print()
        for i in range(n_cards):
            print(f"|__{self.cards[i].value}|", end="\t")
        print()




# class Deck(Hand):
#     def __init__(self, cards):
#         super().__init__(cards)
#     def Deck(self):
#
#     def mix_cards(self):
#
#     def deal_hand(self, n):




