import Card
import Hand
import Player

cards = []
for k in range(4):
    if k == 0:
        symbol="♧"
    elif k == 1:
        symbol="♡"
    elif k == 2:
        symbol="♢"
    else:
        symbol="♤"
    for i in range(13):
        if i+1 == 1:
            cards.append(Card.Card(symbol, "A"))
        elif i+1 == 13:
            cards.append(Card.Card(symbol, "K"))
        elif i+1 == 12:
            cards.append(Card.Card(symbol, "Q"))
        elif i+1 == 11:
            cards.append(Card.Card(symbol, "J"))
        else:
            cards.append(Card.Card(symbol, f"{i + 1}"))

default_deck = Hand.Deck(cards)

default_deck.mix_cards()
# player1 = Player.Player(Hand.Hand(default_deck.deal_hand()), 1000)
# krupier = Player.Krupier(Hand.Hand(default_deck.deal_hand()), 1000, default_deck)
# player1.get_hand().print_cards()
# print(player1.get_hand().calculate_value())
# krupier.get_hand().print_cards()
# krupier.deal_krupier_card()
# krupier.deal_card(player1)
# print("-"*25)
# player1.get_hand().print_cards()
# print(player1.get_hand().calculate_value())
# krupier.get_hand().print_cards()
default_deck.mix_cards()
rules = """
Rules:
Try to get as close to 21 without going over.
Kings, Queens, and Jacks are worth 19 points.
Aces are worth 1 or 11 points.
Cards 2 through 10 are worth their face value.
(H)it to take another card.
(S)tand to stop taking cards.
On your first play, you can (D)ouble down to increase your bet
but must hit exactly one more time before standing.
In case of a tie, the bet is returned to the playera
The dealer stops hitting at 17.
"""
print(rules)
player1 = Player.Player(Hand.Hand(default_deck.deal_hand()), 5000)
krupier = Player.Krupier(Hand.Hand(default_deck.deal_hand()), 1000, default_deck)
while(True):    
    print("Money: ",player1.get_money())
    print(f"How much do you bet? (1-{player1.get_money()}) or QUIT")
    option = input("> ")
    if option == "QUIT":
        break
    else:
        bet = int(option)
    print("Bet: ",bet)
    player1.bet(bet)
    print("DEALER: ???")
    krupier.get_hand().print_cards()
    print()
    print("PLAYER: ",player1.get_hand().calculate_value())
    player1.get_hand().print_cards()
