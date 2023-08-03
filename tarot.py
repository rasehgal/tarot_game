from deck import deck


#initialize deck with starter cards
#STARTER_PACK = [("the lovers","descrthelovers"), ("the healer","descrthehealer"), ("the tower","towerdesc"), ("card_four","means something"), ("card_five","something else")]
STARTER_PACK = [("one","one"),("two","two"),("three","three"),("four","four"),("five","five"),("six","six"),("seven","seven"),("eight","eight"),("nine","nine"),("ten","ten")]

TDECK = deck() #creates deck

#adds starter cards to deck
for name, desc in STARTER_PACK:
	TDECK.add_card(name,desc)

# define various tarot spreads in an interactive way, allow
# for upside down cards, different orientations, and diff categories
# and interpretations
def spread(n, r = None): 
    if r == 0:
        repl = r
    else: repl = 1
    TDECK.shuffle_deck()
    decks = (TDECK.draw_cards(n, repl))
    new_spread = decks[1]
    for card, defn in new_spread:
        print(card + "-->" + defn)


#eventually create interactivity 
#why won't you add to my commit
#def main(): 
#TDECK.print_deck()
#print("DRAWING")
#spread(5, 0)
#print("DECK:")
#TDECK.print_deck()
#print("SHUFFLING")
#TDECK.shuffle_deck()
#TDECK.print_deck()
#print("DRAWING")
#spread(3,1)
#print("DRAWING")
#spread(2)
#print("END WITH")
#TDECK.print_deck()
