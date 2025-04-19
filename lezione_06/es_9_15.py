'''9-15. Lottery Analysis: Extend the LotteryMachine class you created in Exercise 9-14.

1. Add a method called win(self, my_ticket) that:

    Accepts a ticket (a list of 4 items).
    Repeatedly draws random tickets using the draw_ticket() method.
    Keeps count of how many attempts it takes until a randomly drawn ticket matches my_ticket.
    Returns the number of attempts and the winning ticket.

2. Create a ticket called my_ticket with 4 numbers or letters from the pool.

3. Use the win() method to simulate how many draws it would take for your ticket to win.

4. Print a message showing:

    Your ticket
    The winning ticket
    How many attempts it took to win
'''

import random

class LotteryMachine:
    def __init__(self):
        self.pull:list = list(range(10)) + ['A', 'B', 'C', 'D', 'E']

    def draw_ticket(self)-> list:
        return random.sample(self.pull, 4)

    def win(self, my_ticket:list)->tuple:
        attempts = 0
        while True:
            attempts += 1
            drawn_ticket = self.draw_ticket()
            if set(drawn_ticket) == set(my_ticket):
                return attempts, drawn_ticket

lottery = LotteryMachine()

my_ticket = [3, 'B', 7, 'D']

attempts, winning_ticket = lottery.win(my_ticket)

print("Your ticket:", my_ticket)
print("Winning ticket:", winning_ticket)
print(f"It took {attempts} attempts to win!")


