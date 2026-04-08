from Card import Card
import random

class Deck():
    def __init__(self):
        ranks = Card.RANKS
        suites = Card.SUITS
        deck = []

        # Fixed: Changed 'rank' to 'ranks' to match your variable above
        for rank in ranks:
            for suite in suites:
                card = Card(suit=suite, rank=rank)
                deck.append(card)

        self.deck = deck

    # Fixed: Moved this OUTSIDE of __init__ (un-indented)
    def shuffle(self): 
        newDeck = []
        deck = self.deck

        while True:
            if len(deck) == 1:
                card = deck[0]
                newDeck.append(card)
                break
            
            n = random.randint(0, len(deck) - 1)
            card = deck.pop(n)
            newDeck.append(card)

            print("new deck length", len(newDeck))
            print("old deck length", len(deck))
            for card_obj in newDeck:
                card_obj.printCard()
                print("--")
        
        self.deck = newDeck

    def print_deck(self): # Added self
        deck = self.deck
        print("deck size is ", len(deck))

        print("_________________")
        for card in deck:
            card.printCard()
            print("------------------")

    def burn_card(self):
        print("before taking card on the deck")
        self.printCard()
        print("After buring")
        top_card = self.deck[0]
        self.deck.pop(0)
        self.deck.append(top_card)
        self.print_deck()
        pass
    def give_card(self):
        top_card = self.deck[0]
        self.deck.pop(0)
        return top_card
    

if __name__ == "__main__":
    d1 = Deck()
    # Now you can actually call it!
    d1.shuffle()
    card = d1.give_card()
    print("given card is")
    card.printCard()
    d1.print_deck()



