#! python3

print("Task 5.3")

alien_color = 'green'
if alien_color == 'green':
    print('You guessed. You get 5 points.')
print('\n')
alien_color = 'yellow'
if alien_color == 'green':
    print('You guessed. You get 5 points.')

print("Task 5.4")

alien_color = 'green'
if alien_color == 'green':
    print('You get 5 points for shooting down an alien.')
else:
    print("You don't get 5 points for shooting down an alien.")
print('\n')
alien_color = 'yellow'
if alien_color == 'green':
    print('You get 5 points for shooting down an alien.')
else:
    print("You don't get 5 points for shooting down an alien.")

print("Task 5.5")

alien_color = 'green'
if alien_color == 'green':
    print('You get 5 points for shooting down an alien.')
elif alien_color == 'yellow':
    print('You get 10 points for shooting down an alien.')
elif alien_color == 'red':
    print('You get 15 points for shooting down an alien.')
else:
    print("You don't get 5 points for shooting down an alien.")
print('\n')
alien_color = 'yellow'
if alien_color == 'green':
    print('You get 5 points for shooting down an alien.')
elif alien_color == 'yellow':
    print('You get 10 points for shooting down an alien.')
elif alien_color == 'red':
    print('You get 15 points for shooting down an alien.')
else:
    print("You don't get 5 points for shooting down an alien.")
print('\n')
alien_color = 'red'
if alien_color == 'green':
    print('You get 5 points for shooting down an alien.')
elif alien_color == 'yellow':
    print('You get 10 points for shooting down an alien.')
elif alien_color == 'red':
    print('You get 15 points for shooting down an alien.')
else:
    print("You don't get 5 points for shooting down an alien.")
print('\n')
alien_color = 'black'
if alien_color == 'green':
    print('You get 5 points for shooting down an alien.')
elif alien_color == 'yellow':
    print('You get 10 points for shooting down an alien.')
elif alien_color == 'red':
    print('You get 15 points for shooting down an alien.')
else:
    print("You don't get 5 points for shooting down an alien.")
print('\n')

print("Task 5.6")

age = 32
if age <= 2:
    print('You are a baby')
elif age < 4:
    print('You are toddler')
elif age < 13:
    print('You are kid')
elif age < 20:
    print('You are teenager')
elif age < 65:
    print('You are adult')
else:
    print('You are elder')

print("Task 5.7")

favorite_fruits = ['grapes', 'bananas', 'kiwis']
if 'bananas' in favorite_fruits:
    print("You really like bananas!")
if 'apples' in favorite_fruits:
    print("You really like apples!")
if 'blueberries' in favorite_fruits:
    print("You really like blueberries!")
if 'kiwis' in favorite_fruits:
    print("You really like kiwis!")
if 'peaches' in favorite_fruits:
    print("You really like peaches!")