
class Player():
    def __init__(self, hand, money):
        self.hand = hand
        self.money = money
    def bet(self, amount):
        self.money -= amount
    def get_hand(self):
        return self.hand
    def get_money(self):
        return self.money
class Krupier(Player):
    def __init__(self, hand, money,deck):
        Player.__init__(self, hand, money)
        self.deck = deck
    def deal_hand(self, player):

    def deal_krupier_hand(self):

