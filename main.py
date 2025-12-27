import Card
import Hand
import Player
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"
cards = []
amount_cards_multiplier = 1 # Change to increase cards amount by default 52 cards per deck
for j in range(amount_cards_multiplier):
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

rules = f"""
{BOLD}=== BLACKJACK RULES ==={RESET}
• Try to get as close to 21 without going over.
• Kings, Queens, and Jacks are worth 10 points.
• Aces are worth 1 or 11 points.
• Cards 2 through 10 are worth their face value.
• (H)it to take another card.
• (S)tand to stop taking cards.
• (D)ouble down on first play.
• In case of a tie, the bet is returned to the player.
• Dealer stands on 17.
"""
print(rules)
player1 = Player.Player(Hand.Hand(default_deck.deal_hand()), 5000)
krupier = Player.Krupier(Hand.Hand(default_deck.deal_hand()), 5000, default_deck)
def print_match(rol=None):
    print(f"{BOLD}{CYAN}DEALER:{RESET}",
          f"{'???' if rol == 'krupier' else krupier.get_hand().calculate_value()}")
    krupier.get_hand().print_cards(rol)
    print()
    print(f"{BOLD}{GREEN}PLAYER:{RESET}", player1.get_hand().calculate_value())
    player1.get_hand().print_cards()
    print("-" * 40)

while(True):    
    try:
        print(f"{GREEN}Money:{RESET} {player1.get_money()}")
        print(f"How much do you bet? (1-{player1.get_money()}) or QUIT")
        option = input("> ")
        if option.upper() == "QUIT" or option.upper() == "Q":
            break
        else:
            bet = int(option)
            while bet > player1.get_money():
                print(f"You don't have enough money. Try another amount (1-{player1.get_money()}).")
                option = input("> ")
                bet = int(option)

        print("Bet: ",bet)
        player1.bet(bet)
        print_match(rol="krupier")
        move=""
        while(player1.get_hand().calculate_value()<21 and krupier.get_hand().calculate_value()<21):
            print("(H)it, (S)tand, (D)ouble down")
            move = input("> ")
            if move.upper() == "H":
                krupier.deal_card(player1)
                print(f"You drew {CYAN}{player1.get_hand().get_card(-1).get_value()} of {player1.get_hand().get_card(-1).get_suit()}{RESET}")
                print("--snip--")
                print_match(rol="krupier")
            elif move.upper() == "S":
                break
            elif move.upper() == "D":
                if player1.get_money() >= bet:
                    print(f"{BOLD}{YELLOW}-- DOUBLE DOWN --{RESET}")
                    print(f"Your bet increases {bet*2}")
                    player1.bet(bet)
                    bet*=2
                    krupier.deal_card(player1)
                    print_match()
                    break
                else:
                    print("You don't have enough money")

        while krupier.get_hand().calculate_value() < 17 and player1.get_hand().calculate_value() < 22:
            krupier.deal_krupier_card()
            print(f"Dealer drew {RED}{krupier.get_hand().get_card(-1).get_value()} of {krupier.get_hand().get_card(-1).get_suit()}{RESET}")
            print("--snip--")
            print_match()
        if krupier.get_hand().calculate_value() == player1.get_hand().calculate_value() and player1.get_hand().calculate_value() < 22 and krupier.get_hand().calculate_value() < 22:
            print("--snip--")
            print_match()
            print(f"{YELLOW}Tie. Bet returned.{RESET}")
        else:    
            if player1.get_hand().calculate_value() > 21 or krupier.get_hand().calculate_value() == 21 or krupier.get_hand().calculate_value() > player1.get_hand().calculate_value() and krupier.get_hand().calculate_value() < 22:
                print("--snip--")
                print_match()
                print(f"{RED}You lose{RESET}")
                bet=0
            else:
                print("--snip--")
                print_match()
                print(f"{GREEN}You win!{RESET}")
                bet*=2
            
        player1 = Player.Player(Hand.Hand(default_deck.deal_hand()), player1.get_money()+bet)
        krupier = Player.Krupier(Hand.Hand(default_deck.deal_hand()), krupier.get_money(), default_deck)

        if player1.get_money()<1:
            print("You don't have money.")
            break
    except IndexError:
        print("There are not cards to continue playing")
        break
    except ValueError:
        print("Enter a valid amount to bet or QUIT/quit/q")
print("Byee...")
