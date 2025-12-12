import Card
import Hand
import Player
# ♤, ♡, ♢, ♧
carta1 = Card.Card("♧", "K")
carta2 = Card.Card("♡", "7")
carta3 = Card.Card("♢", "10")
carta4 = Card.Card("♢", "8")
cartas = [carta1, carta2, carta3,carta4]

jugador1 = Player.Player(cartas, 1000)
mano_jugador1 = Hand.Hand(jugador1.hand)
print("Player 1 Hand: ", mano_jugador1.calculate_value())
mano_jugador1.print_cards()
