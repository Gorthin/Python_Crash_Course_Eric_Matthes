#! python3

print("Task 4.10")
animals = ['dog', 'cat', 'monkey', 'elephant', 'tiger', 'lion']
for animal in animals:
    print(f'{animal.title()} is a good friend.')

print("\nAll of this animals are great!")
print(f"\nFirstly three elements of animal: {animals[0:3]}.")
print(f"\nFirstly four elements of animal: {animals[1:5]}.")
print(f"\nLast three elements of animal: {animals[3:]}.")

print("Task 4.11")
pizzas = ['pepperoni', 'capricosa', 'rimini']
for pizza in pizzas:
    print(f"\nI like pizza' {pizza.title()}")

friend_pizzas = pizzas[:]
pizzas.append('shorma')
friend_pizzas.append('farmer')

for pizza in pizzas:
    print(f"\nMy favorite pizza:' {pizza.title()}")

for pizza in friend_pizzas:
    print(f"\nFavorite pizza my friend:' {pizza.title()}")

print("Task 4.12")
my_foods = ['pizza', 'falafel', 'cannolo']
print('My favorites foods:')
for food in my_foods:
    print(f"- {food}")

print("Task 4.12")
buffet = ('pizza', 'canneloni', 'risotto', 'falafel', 'ice')
print('Foods of restaurant:')
for food in buffet:
    print(f"- {food}")
#buffet[0] = 'salmon burger'

buffet = ('pizza', 'smoked salmon', 'nugets', 'falafel', 'ice')
print("\nOur menu has been updated.")
print("You can now choose from the following items:")
for food in buffet:
    print(f"- {food}")