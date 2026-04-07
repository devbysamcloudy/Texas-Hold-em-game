class Card:
    def __init__(self, suit, rank):
        
        acceptedRanks = ["A","K","Q","J","10","9","8","7","6","5","4","3","2"]
        acceptedSuits = ["HEARTS", "DIAMONDS", "SPADES", "CLUBS"]

        if not isinstance(suit, str):
            raise TypeError(f"Suit expected to be a string, got {type(suit)}")

        if not isinstance(rank, str):
            raise TypeError(f"Rank expected to be a string, got {type(rank)}")

        suitUpper = suit.upper()
        rankUpper = rank.upper()
        if rankUpper in acceptedRanks:
            pass
        else:
            raise TypeError(f"Added a rank not in rank list {acceptedRanks}, got {rank}")

        if suitUpper in acceptedSuits:
            pass
        else:
            raise TypeError(f"Added a suit not in suit list {acceptedSuits}, got {suit}")
        
        self.suit = suitUpper
        self.rank = rankUpper

    def printCard(self):
        print("Rank", self.rank)
        print("Suit", self.suit)


if __name__ == "__main__":
           card1 = Card("Hearts", "A")
           card1.printCard()

           Card2 = Card("Spades", "10")
           Card2.printCard()