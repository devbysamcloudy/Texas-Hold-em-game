import random
import time
from itertools import combinations


class Round:
    def __init__(self, human, pc, deck, pot=0):
        self.human = human
        self.pc = pc
        self.pot = pot
        self.table_cards = [deck.give_card() for _ in range(5)]
        self.human_selected = []
        self.pc_selected = []

    def _fmt(self, card):
        return f"[{card.rank} of {card.suit}]"

    def _score(self, cards):
        counts = {}
        for c in cards:
            counts[c.rank] = counts.get(c.rank, 0) + 1
        order = {"A":14,"K":13,"Q":12,"J":11,"10":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2}
        return (max(counts.values()), max(order.get(c.rank, 0) for c in cards))

    def _best_hand(self, cards):
        return max(combinations(cards, 3), key=self._score)

    def _deal(self):
        self.human_selected = self._best_hand(self.human.cards + self.table_cards)
        self.pc_selected    = self._best_hand(self.pc.cards    + self.table_cards)

    def play(self):
        print("\n─── NEW ROUND ───")
        print("Cards on the table:", ", ".join(self._fmt(c) for c in self.table_cards))
        print("Your cards:", ", ".join(self._fmt(c) for c in self.human.cards))

        self._deal()
        print("Your best 3:", ", ".join(self._fmt(c) for c in self.human_selected))

        print(f"\nPot: ${self.pot}  |  Your balance: ${self.human.amount}")
        action = input("bet [amount], pass, or fold: ").strip().lower()
        if action == "fold":
            print("You folded. PC takes the pot.")
            self.pc.amount += self.pot
            return
        if action.startswith("bet ") and action[4:].isdigit():
            bet = int(action[4:])
            if 1 <= bet <= self.human.amount:
                self.human.amount -= bet
                self.pot += bet
                time.sleep(1)
                if self.pc.amount >= bet:
                    self.pc.amount -= bet
                    self.pot += bet
                    print(f"PC matches. Pot: ${self.pot}")
                else:
                    print("PC can't match — you win!")
                    self.human.amount += self.pot
                    return

        print("\n─── CARDS DOWN ───")
        print("Your hand:", ", ".join(self._fmt(c) for c in self.human_selected))
        print("PC's hand:", ", ".join(self._fmt(c) for c in self.pc_selected))
        hs, ps = self._score(self.human_selected), self._score(self.pc_selected)
        if hs > ps:
            print(f"You win! +${self.pot}"); self.human.amount += self.pot
        elif ps > hs:
            print(f"PC wins! +${self.pot}"); self.pc.amount += self.pot
        else:
            split = self.pot // 2
            print(f"Draw — you each get ${split}")
            self.human.amount += split; self.pc.amount += split
        print(f"Your balance: ${self.human.amount}  |  PC: ${self.pc.amount}")
