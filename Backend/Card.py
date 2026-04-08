class Card:
    RANKS = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2"]
    SUITS = ["HEARTS", "DIAMONDS", "SPADES", "CLUBS"]

    def __init__(self, suit, rank):
        # 1. Type checking
        if not isinstance(suit, str) or not isinstance(rank, str):
            raise TypeError("Suit and Rank must be strings")

        suit_upper = suit.upper()
        rank_upper = rank.upper()

        # 2. Validation against the class constants
        if rank_upper not in Card.RANKS:
            raise ValueError(f"Invalid rank: {rank_upper}. Must be one of {Card.RANKS}")

        if suit_upper not in Card.SUITS:
            raise ValueError(f"Invalid suit: {suit_upper}. Must be one of {Card.SUITS}")
        
        # 3. Assignment
        self.suit = suit_upper
        self.rank = rank_upper

    def printCard(self):
        print(f"Rank: {self.rank}")
        print(f"Suit: {self.suit}")


if __name__ == "__main__":
    card1 = Card("Hearts", "A")
    card1.printCard()

    card2 = Card("Spades", "3")
    card2.printCard()

    