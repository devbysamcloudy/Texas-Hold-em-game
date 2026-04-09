import random
import time


class Round:
    def __init__(self, human, pc, deck, pot=0):
        self.human = human
        self.pc = pc
        self.deck = deck
        self.pot = pot

        self.community_cards = [deck.give_card() for _ in range(5)]

        self.human_selected = []
        self.pc_selected = []

    def _format_card(self, card):
        return f"[{card.rank} of {card.suit}]"

    def _show_available_cards(self):
        all_cards = self.human.cards + self.community_cards
        print("\n Your available cards:")
        for i, card in enumerate(all_cards):
            print(f"  {i + 1}. {self._format_card(card)}")
        print()

    def _show_community_cards(self):
        print("\n Community cards on the table:")
        for card in self.community_cards:
            print(f"  {self._format_card(card)}")
        print()

    def human_select_cards(self):
        all_cards = self.human.cards + self.community_cards
        self._show_available_cards()

        print("Select 3 cards by typing their RANK (e.g. A, Q, 10, K, 7)")
        print("Available ranks:", [card.rank for card in all_cards])

        selected = []
        remaining = list(all_cards) 

        while len(selected) < 3:
            rank_input = input(f"Pick card {len(selected) + 1}/3 → ").strip().upper()

            match = None
            for card in remaining:
                if card.rank == rank_input:
                    match = card
                    break

            if match:
                selected.append(match)
                remaining.remove(match)
                print(f"  Added {self._format_card(match)}")
            else:
                available_ranks = [card.rank for card in remaining]
                print(f"   '{rank_input}' not found in your available cards.")
                print(f"     Available: {available_ranks}")

        self.human_selected = selected
        print("\n Your selected hand:")
        for card in self.human_selected:
            print(f"  {self._format_card(card)}")


    def pc_select_cards(self):
        print("\n PC is choosing its 3 cards...")
        time.sleep(1.5)

        all_cards = self.pc.cards + self.community_cards
        self.pc_selected = random.sample(all_cards, 3)

        print("PC has placed its cards face down.")


    def betting_round(self):
        print(f"\n Current pot: {self.pot}")
        print(f"   Your balance: {self.human.amount}")

        while True:
            bet = input("Place your bet (or type 'fold' to forfeit): ").strip().lower()

            if bet == "fold":
                print("You folded. PC wins the pot!")
                self.pc.amount += self.pot
                return False 

            if bet.isdigit():
                bet = int(bet)
                if 1 <= bet <= self.human.amount:
                    self.human.amount -= bet
                    self.human.update_amount(bet)
                    self.pot += bet

                    print("\n PC is deciding...")
                    time.sleep(1)
                    if self.pc.amount >= bet:
                        self.pc.amount -= bet
                        self.pc.update_amount(bet)
                        self.pot += bet
                        print(f"PC matches your bet of {bet}.")
                    else:
                        print("PC can't match. PC folds. You win the pot!")
                        self.human.amount += self.pot
                        return False

                    print(f"Total pot: {self.pot}")
                    return True  
                else:
                    print(f"Enter a value between 1 and {self.human.amount}.")
            else:
                print("Type a number or 'fold'.")

    def _count_matches(self, cards):
        """
        Returns the highest number of same-rank cards in a hand.
        e.g. [A, A, K] → 2 (a pair of Aces)
             [7, 7, 7] → 3 (three of a kind)
             [Q, K, A] → 1 (no matches)
        """
        rank_counts = {}
        for card in cards:
            rank_counts[card.rank] = rank_counts.get(card.rank, 0) + 1
        return max(rank_counts.values())

    def _rank_value(self, rank):
        """Returns numeric value of a rank for tiebreaking."""
        order = {"A": 14, "K": 13, "Q": 12, "J": 11,
                 "10": 10, "9": 9, "8": 8, "7": 7,
                 "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}
        return order.get(rank, 0)

    def _best_card_value(self, cards):
        """Returns the highest single card value in a hand."""
        return max(self._rank_value(card.rank) for card in cards)

    def detect_winner(self):
        print("\n============SHOWDOWN ================")

        print("\n Your hand:")
        for card in self.human_selected:
            print(f"  {self._format_card(card)}")

        print("\ PC's hand:")
        for card in self.pc_selected:
            print(f"  {self._format_card(card)}")

        human_score = self._count_matches(self.human_selected)
        pc_score = self._count_matches(self.pc_selected)

        print(f"\n Your best match: {human_score} of a kind")
        print(f"PC's best match: {pc_score} of a kind")

        if human_score > pc_score:
            winner = "human"
        elif pc_score > human_score:
            winner = "pc"
        else:

            human_best = self._best_card_value(self.human_selected)
            pc_best = self._best_card_value(self.pc_selected)

            print(f"\n Tie on matches! Tiebreak by highest card...")
            print(f"   Your highest: {human_best} | PC's highest: {pc_best}")

            if human_best > pc_best:
                winner = "human"
            elif pc_best > human_best:
                winner = "pc"
            else:
                winner = "draw"

        print("\n==========================================")

        if winner == "human":
            print(f" YOU WIN! You take the pot of {self.pot}!")
            self.human.amount += self.pot
        elif winner == "pc":
            print(f" PC WINS! PC takes the pot of {self.pot}.")
            self.pc.amount += self.pot
        else:
            split = self.pot // 2
            print(f"It's a DRAW! Pot split — you each get {split}.")
            self.human.amount += split
            self.pc.amount += split

        print(f"\n Your balance: {self.human.amount}")
        print(f" PC balance:   {self.pc.amount}")
        print("==========================================\n")

        return winner


    def play(self):
        print("\n═══════════════ NEW ROUND ═══════════════")
        self._show_community_cards()

        self.human_select_cards()
        self.pc_select_cards()

        proceed = self.betting_round()
        if not proceed:
            return 

        return self.detect_winner()