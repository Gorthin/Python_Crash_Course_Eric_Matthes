#! python3

print("Task 7.4")

prompt = '\nGive me a toppings Your pizza'
prompt += "\n(If you stop a giving a topping, write a 'end'"

while True:
    topping = input(prompt)
    if topping != 'end':
        print(f"  I add {topping} to your pizza.")
    else:
        break

print("Task 7.5")

prompt = '\nGive me your age (if you like a stop write: end)'

while True:
    age = input(prompt)
    if age == 'end':
        break
    age = int(age)

    if age < 3:
        print('Ticket is a free')
    elif age < 12:
        print('Cost of ticket is a 10 dolars')
    else:
        print('Cost of ticket is a 15 dolars')

print("Task 7.6")



print("Task 7.6")

y = 0
while y < 30:
    print(y)
