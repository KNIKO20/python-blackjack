import Card
import Hand
# ♤, ♡, ♢, ♧
carta1 = Card.Card("♧", "K")
carta2 = Card.Card("♡", "7")
carta3 = Card.Card("♢", "8")
carta4 = Card.Card("♢", "8")
cartas = [carta1, carta2, carta3,carta4]
mano = Hand.Hand(cartas)
mano.print_cards()
