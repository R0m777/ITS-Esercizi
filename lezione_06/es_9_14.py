'''9-14.
Lottery: Create a class LotteryMachine that holds a list containing a series of 10 numbers and 5 letters. 
Implement a method to randomly select 4 items (numbers or letters) from this list to draw a winning ticket. 
Finally, implement a method to display a message saying that any ticket matching the winning 4 items wins a prize.'''

import random

class LotteryMachine:
    def __init__(self):
        letters:list = ['A', 'B', 'C', 'D', 'E']
        numbers:list = list(range(10)) 
        self.pull:int = numbers + letters

    def winning_ticket(self)->int:
        self.winning_ticket = random.sample(self.pull, 4)
        return self.winning_ticket

    def display_winner_message(self)->None:
        print("\nWinning Ticket Drawn")
        print("Winning combination:", self.winning_ticket)
        print("If your ticket matches these 4 items (in any order), you win a prize!")

# Create instance and draw a ticket
lottery = LotteryMachine()
lottery.winning_ticket()
lottery.display_winner_message()

