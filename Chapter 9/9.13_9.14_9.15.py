#! python3

print("Task 9.13")

from random import randint

class Die():
    """Represent a die, which can be rolled."""
    def __init__(self, sides = 6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)

sides6 = Die()

results = []
for roll in range(10):
    result = sides6.roll_die()
    results.append(result)
print("10 rolls of a 6-sided die:")
print(results)

sides10 = Die(sides = 10)

results = []
for roll in range(10):
    result = sides10.roll_die()
    results.append(result)
print("10 rolls of a 10-sided die:")
print(results)

sides20 = Die(sides = 20)

results = []
for roll in range(10):
    result = sides20.roll_die()
    results.append(result)
print("10 rolls of a 20-sided die:")
print(results)

print("Task 9.13")

from random import choice

lottery_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
win_ticket = []

print('Win ticket is: ')

while len(win_ticket) < 4:
    pull = choice(lottery_numbers)

    if pull not in win_ticket:
        print(f"  We pulled a: {pull}!")
        win_ticket.append(pull)
print(f'Win ticket is {win_ticket}')

print("Task 9.14")

from random import choice

def get_winning_ticket(lottery_numbers):
    """Return a winning ticket from a set of possibilities."""
    win_ticket = []

    while len(win_ticket) < 4:
        pull = choice(lottery_numbers)

        if pull not in win_ticket:
            win_ticket.append(pull)

    return win_ticket

def check_ticket(played_ticket, winning_ticket):
    for element in played_ticket:
        if element not in winning_ticket:
            return False
    return True

def make_random_ticket(lottery_numbers):
    """Return a random ticket from a set of possibilities."""
    ticket = []
    # We don't want to repeat numbers or letters, so we'll use a while loop.
    while len(ticket) < 4:
        pull = choice(lottery_numbers)

        # Only add the pulled item to the ticket if it hasn't already
        #   been pulled.
        if pull not in ticket:
            ticket.append(pull)

    return ticket


lottery_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']
win_ticket = get_winning_ticket(lottery_numbers)

plays = 0
won = False

max_tries = 1_000_000

while not won:
    new_ticket = make_random_ticket(lottery_numbers)
    won = check_ticket(new_ticket, win_ticket)
    plays += 1
    if plays >= max_tries:
        break

if won:
    print("We have a winning ticket!")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {win_ticket}")
    print(f"It only took {plays} tries to win!")
else:
    print(f"Tried {plays} times, without pulling a winner. :(")
    print(f"Your ticket: {new_ticket}")
    print(f"Winning ticket: {win_ticket}")