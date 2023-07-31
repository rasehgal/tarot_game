from deck import deck


#initialize deck with starter cards
STARTER_PACK = [("the lovers","descrthelovers"), ("the healer","descrthehealer"), ("the tower","towerdesc"), ("card_four","means something"), ("card_five","something else")]

TDECK = deck() #creates deck

#adds starter cards to deck
for name, desc in STARTER_PACK:
	TDECK.add_card(name,desc)

# define various tarot spreads in an interactive way, allow
# for upside down cards, different orientations, and diff categories
# and interpretations
def three_spread(): return 0
def five_spread(): return 0
def future(): return 0
def single_draw(): return 0


#eventually create interactivity 
#why won't you add to my commit
def main(): 
    #deck.three_spread()
    #deck.print_deck()
    #deck.three_spread()
    TDECK.print_deck()
    TDECK.add_card("foo", "bar")
    print("added")
    TDECK.print_deck()
    TDECK.remove_card("foo")
    print("removed")
    TDECK.print_deck()
