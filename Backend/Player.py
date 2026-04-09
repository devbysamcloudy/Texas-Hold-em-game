import random
import time

class Player():
    def __init__(self, type= "pc", cards =[], total_amount_bet = 0, name = "", amount = 0):
        self.name = name
        self.type = type
        self.cards = cards
        self.total_amount_bet = total_amount_bet
        self.amount = amount


    def place_initial_bet(self):
        while True:
            amount = input("Enter the amount you want to bet: ")

            if amount.isdigit():
                n = int(amount)
                if n > 0 and n <= self.amount:
                    self.amount = self.amount - n
                    return n

                print("Invalid amount. Please enter a positive number less than or equal to your current amount.")
                print (f"amount must range from 1 to {self.amount}")
                print("Please try again.")

            else:
                print(f"Enter a valid amount between 1 and {self.amount}")

    def auto_match_or_raise(self,amount):
        print("PC is thinking...")
        time.sleep(2)
        to_do = random.randint(1,2)
        raise_amount = random.randint(10, 250)

        if raise_amount > self.amount:
            to_do = 1

        if to_do == 1:
            if self.amount >= amount:
                self.amount - amount
                print(f"PC has matched your bet of {amount}")
                return amount

            else:
                return "l"

        self.amount = self.amount - raise_amount
        print("I am raising the bet by ", raise_amount)
        return raise_amount

    def update_amount(self, amount):
        self.total_amount_bet = self.total_amount_bet + amount

    def reset_amount_bet(self):
        self.total_amount_bet = 0
        
                          

        