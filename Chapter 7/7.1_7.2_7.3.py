#! python3

print("Task 7.1")

car = input("What kind of car would you like a buy?")
print(f'Let me see if i can find you a {car}')

print("Task 7.2")

number_person = input('How many people do you want a table for?')
number_person = int(number_person)

if number_person > 8:
    print('You must wait for a table')
else:
    print('Come with me to the table')

print("Task 7.3")

number = input('Please give me any number')
number = int(number)

if number % 10 == 0:
    print('This number is a multiple of 10.')
else:
    print('This number is not a multiple of 10.')