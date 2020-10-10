#! python3

print("Task 5.8")

usernames = ['rick', 'morty', 'john', 'admin', 'barry']
for username in usernames:
    if username == 'admin':
        print(f'Hello {username}. Do you want look at the today report? ')
    else:
        print(f'Thank you {username.title()} for you logged')

print("Task 5.9")

usernames = []
if usernames:
    for username in usernames:
        if username == 'admin':
            print(f'Hello {username}. Do you want look at the today report? ')
        else:
            print(f'Thank you {username.title()} for you logged')
else:
    print('We need any user!')

print("Task 5.10")

current_users = ['Carrol', "Rick", 'Morty', 'John', 'Amy']
new_users = ['Gary', "peter", 'morty', 'rick', 'Anna']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'{new_user.title()} change you username')
    else:
        print(f'{new_user.title()} you can used this username')

print("Task 5.11")

numbers = list(range(1,10))
for number in numbers:
    if number == '1':
        print(f'{number}st')
    if number == '2':
        print(f'{number}nd')
    if number == '3':
        print(f'{number}rd')
    else:
        print(f'{number}th')