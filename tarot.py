from deck import deck


#initialize deck with starter cards
STARTER_PACK = [("the lovers","descrthelovers"), ("the healer","descrthehealer"), ("the tower","towerdesc"), ("card_four","means something"), ("card_five","something else")]

TDECK = deck() #creates deck

#adds starter cards to deck
for name, desc in STARTER_PACK:
	TDECK.add_card(name,desc)


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
