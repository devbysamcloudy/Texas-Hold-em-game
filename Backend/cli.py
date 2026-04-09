from Game import Game
from Round import Round
from Deck import Deck


def play_game():
    print("===================================")
    print("     Welcome to Texas Hold'em      ")
    print("===================================")

    game = Game()
    human = game.human
    pc = game.pc

    while True:

        if human.amount <= 0:
            print("You're out of money. Game over!")
            break
        if pc.amount <= 0:
            print("PC is out of money. You win the game!")
            break

        human.reset_amount_bet()
        pc.reset_amount_bet()

        print(f"\nYour balance: {human.amount} | PC balance: {pc.amount}")

        while True:
            bet = input("Enter your bet for this round: ").strip()
            if bet.isdigit() and 1 <= int(bet) <= human.amount:
                bet = int(bet)
                break
            print(f"Enter a number between 1 and {human.amount}.")

        human.amount -= bet
        starting_pot = bet * 2 
        print(f"PC matches your bet of {bet}. Pot: {starting_pot}")

        round_ = Round(human, pc, game.deck, pot=starting_pot)
        round_.play()

        again = input("\nPlay another round? (y/n): ").strip().lower()
        if again != "y":
            print("\nThanks for playing!")
            print(f"Final balance — You: {human.amount} | PC: {pc.amount}")
            break

        game.deck = Deck()
        game.deck.shuffle()
        game.deck.shuffle()

        human.cards = [game.deck.give_card(), game.deck.give_card()]
        pc.cards = [game.deck.give_card(), game.deck.give_card()]


if __name__ == "__main__":
    play_game()