#! python3

print("Task 7.8")

sandwich_orders = ['fish', 'vegge', 'roast', 'grilled']
finished_sandwiches = []

while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()
    print(f'I am working on your {current_sandwiches.title()}')
    finished_sandwiches.append(current_sandwiches)

print('All making sandwiches:')
for sandwich in finished_sandwiches:
    print(f'I made {sandwich}')

print("Task 7.9")

sandwich_orders = ['fish', 'pastrami', 'vegge', 'roast', 'pastrami', 'grilled', 'pastrami']
finished_sandwiches = []

print('Sorry we do not have a Pastrami')
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()
    print(f'I am working on your {current_sandwiches.title()}')
    finished_sandwiches.append(current_sandwiches)

print('All making sandwiches:')
for sandwich in finished_sandwiches:
    print(f'I made {sandwich}')

print("Task 7.10")

responses = {}
polling_active = True
name_prompt = '\nHow are you name?'
place_prompt = '\nIf there is any place you would like to visit, what would it be?'
continue_prompt = '\nAnyone else want to answer the question? (yes/no)'

while polling_active:
    name = input(name_prompt)
    place = input(place_prompt)

    responses[name] = place

    repeat = input(continue_prompt)
    if repeat == 'no':
        polling_active = False

print('\nSummary:')
for name, place in responses.items():
    print(f'{name.title()} would like to visit {place.title()}')