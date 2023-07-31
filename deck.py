#basic deck class for tarot/etc


#create class deck
#deck: list of tuples containing card name and a definition/value
class deck:
    def __init__(self):
        #initialize empty list
        self.deck = []

    # print the deck, both names and definitions
    def print_deck(self):
        for card, defn in self.deck:
            #print(card, '->', defn)
            
    #grab index of an existing card in the deck. input is card name.
    def find_card(self, card_name):
        #print(card_name + "- searching")
        for card, desc in self.deck:
            if card == card_name:
               #print("found " + card)
               return self.deck.index((card_name, desc))
        #print("not found: " + card)
        return 0

    # add a new card item to this list. requires the name and description parameters
    def add_card(self, card_name, card_description):
        new_card = (card_name, card_description)
        self.deck.append(new_card)

    # "draw" cards from the deck-- removes {count} list items off of the list and prints values
    #TO-DO take in whether to pop or replace
    def draw_cards(self, count):
		#if there are fewer than this many cards left, error
        if len(self.deck) < count: return 0
		#iterate through the deck for the number of cards chosen (count)
        # print the cards for viewing and remove from the stack
        for card, defn in (self.deck[:count]):
            print(card, '-->', defn)
            self.deck.remove((card,defn))
            
    # remove card by way of indexing function
    # TO-DO; make this consistent across functions
    def remove_card(self, card_name):
        index = self.find_card(card_name)
        self.deck.pop(index)
        return 0

    # shuffle deck, mixing order of cards for new drawing if desired
    def shuffle(self): return 0

    # TO-DO: have a user option to either pop cards off the list when drawing, or to "return" them to the deck

    

