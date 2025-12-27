import random
class Hand:
    def __init__(self, cards):
        self.cards = cards
    def add_card(self, card):
        self.cards.append(card)
    def calculate_value(self):
        value = 0
        check_aces = 0
        for card in self.cards:
            if card.value == "K" or card.value == "J" or card.value == "Q" :
                value += 10
            elif card.value == "A" :
                check_aces+=1
            else:
                value += int(card.value)
        for i in range(check_aces):   
            if value+11 > 21:
                value+=1
            else:
                value+=11
        return value
    def get_card(self, n_card):
        # if (self.cards[n_card].value == "10"):
        #     print("_"*5)
        #     print(f"|{self.cards[n_card].value} |")
        #     print(f"| {self.cards[n_card].suit} |")
        #     print(f"|_{self.cards[n_card].value}|")
        # else:
        #     print("_" * 5)
        #     print(f"|{self.cards[n_card].value}  |")
        #     print(f"| {self.cards[n_card].suit} |")
        #     print(f"|__{self.cards[n_card].value}|")
        return self.cards[n_card]

    def print_cards(self, rol=None):
        n_cards = len(self.cards)

        for i in range(n_cards):
            print(f" ___", end="\t")
        print()
        for i in range(n_cards):
            if i == 0 and rol=="krupier":
                print(f"|## |", end="\t")
            elif self.cards[i].value == "10":
                print(f"|{self.cards[i].value} |", end="\t")
            else:
                print(f"|{self.cards[i].value}  |", end="\t")
        print()
        for i in range(n_cards):
            if i == 0 and rol=="krupier":
                print(f"|###|", end="\t")
            else:
                print(f"| {self.cards[i].suit} |", end="\t")
        print()
        for i in range(n_cards):
            if i == 0 and rol=="krupier":
                print(f"| ##|", end="\t")
            elif self.cards[i].value == "10":
                print(f"|_{self.cards[i].value}|", end="\t")
            else:
                print(f"|__{self.cards[i].value}|", end="\t")
        print()

class Deck(Hand):
    count_cards = 0
    def __init__(self, cards):
        super().__init__(cards)
    def mix_cards(self):
        random.shuffle(self.cards)
    def deal_hand(self):
        initial_hand = []
        i=0
        while i < 2:
            initial_hand.append(self.cards[self.count_cards])
            self.count_cards+=1
            i+=1
        return initial_hand
    def draw_card(self):
        card = self.cards[self.count_cards]
        self.count_cards+=1
        return card




