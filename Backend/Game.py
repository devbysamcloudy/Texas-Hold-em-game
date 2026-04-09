from Deck import Deck
from Player import Player

class Game():
    def __init__(self):
        self.main_pot = 0
        self.current_pot = 0
        deck = Deck()
        deck.shuffle()
        deck.shuffle()
        human_cards= [deck.give_card(), deck.give_card()]
        pc_cards = [deck.give_card(), deck.give_card()]

        self.human =Player(type="human",
                           cards = human_cards,
                           total_amount_bet= 0,
                           amount= 2000)
        
        self.pc = Player(type="pc",
                         cards=pc_cards,
                         total_amount_bet=0,
                         name="Sam",
                         amount=2000)
        
        self._turn = "human"
        self.deck = deck

    @property
    def turn(self):
        return self._turn
    
    @turn.setter
    def turn(self, player):
        if player in ["human", "pc"]:
            self._turn = player
        else:
            raise ValueError("Turn must be either 'human' or 'pc'")



if __name__ == "__main__":
    game = Game()
    game.deck.print_deck()
    print("This is the deck")
    print("Pc cards")
    game.pc.cards[0].printCard()
    game.pc.cards[1].printCard()
    print("This is the deck")
    print("Human cards")
    game.human.cards[0].printCard()
    game.human.cards[1].printCard()



                                