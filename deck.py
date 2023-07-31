#basic deck class for tarot/etc
class deck:
    def __init__(self):
        self.deck = []

    def print_deck(self):
        for card, defn in self.deck:
            print(card, '->', defn)
            
    def find_card(self, card_name):
        print(card_name + "- searching")
        for card, desc in self.deck:
            if card == card_name:
               print("found " + card)
               return self.deck.index((card_name, desc))
        print("not found: " + card)
        return 0

    def add_card(self, card_name, card_description):
        new_card = (card_name, card_description)
        self.deck.append(new_card)

    def draw_cards(self, count):
		#if there are fewer than this many cards left, error
        if len(self.deck) < count: return 0
		#else if we want only one card, print just that one card
        for card, defn in (self.deck[:3]):
            print(card, '-->', defn)
            self.deck.remove((card,defn))
            
    def remove_card(self, card_name):
        index = self.find_card(card_name)
        self.deck.pop(index)
        return 0

    

