#! python3

print("Task 10.11")

import json

number = input('Give me your number: ')

filename = 'number.json'
with open(filename, 'w') as f:
    json.dump(number, f)
    print(f'Your number has been saved and will be used later, {number}!')

with open(filename) as f:
    number = json.load(f)
    print(f'Your favorite number is: {number}!')

print("Task 10.12")

import json

filename = 'number.json'
try:
    with open(filename) as f:
        number = json.load(f)
except FileNotFoundError:
    number = input('Give me your number: ')
    with open(filename, 'w') as f:
        json.dump(number, f)
        print(f'Your number has been saved and will be used later, {number}!')
else:
    print(f'Your favorite number is: {number}!')

print("Task 10.13")

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username

def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        correct = input(f"Are you {username}? (y/n) ")
        if correct == 'y':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()