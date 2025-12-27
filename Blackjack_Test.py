# import Card
# import Hand
# import Player
# # ♤, ♡, ♢, ♧

# # Deck
# cards = []
# for k in range(4):
#     if k == 0:
#         symbol="♧"
#     elif k == 1:
#         symbol="♡"
#     elif k == 2:
#         symbol="♢"
#     else:
#         symbol="♤"
#     for i in range(13):
#         if i+1 == 1:
#             cards.append(Card.Card(symbol, "A"))
#         elif i+1 == 13:
#             cards.append(Card.Card(symbol, "K"))
#         elif i+1 == 12:
#             cards.append(Card.Card(symbol, "Q"))
#         elif i+1 == 11:
#             cards.append(Card.Card(symbol, "J"))
#         else:
#             cards.append(Card.Card(symbol, f"{i + 1}"))
# # print(cards[8].show_card())
# # print(cards[13].show_card())
# # print(cards[26].show_card())
# # print(cards[39].show_card())

# default_deck = Hand.Deck(cards)
# # default_deck.show_card(51)
# # default_deck.print_cards()
# default_deck.mix_cards()
# # default_deck.print_cards()
# # default_deck.show_card(51)
# player1 = Player.Player(Hand.Hand(default_deck.deal_hand()), 1000)
# krupier = Player.Krupier(Hand.Hand(default_deck.deal_hand()), 1000, default_deck)
# # default_deck.deal_hand()[0].show_card()
# player1.get_hand().print_cards()
# print(player1.get_hand().calculate_value())
# krupier.deal_card(player1)
# print("-"*25)
# player1.get_hand().print_cards()
# print(player1.get_hand().calculate_value())


# player1.get_hand()[0].show_card()
# player1.get_hand()[-1].show_card()

# mano_jugador1 = jugador1.get_hand
# print("Player 1 Hand: ", mano_jugador1.calculate_value())
# mano_jugador1.print_cards()
