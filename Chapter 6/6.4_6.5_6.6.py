#! python3

print("Task 6.4")

glossary = {
    'linux' : 'software',
    'variable' : 'value that may vary',
    'zen python' : 'rules of a good python programmer',
    'function range()' : 'generating numbers',
    'lists' : 'a collection of different values',
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'list': 'A collection of items in a particular order.',
    'loop': 'Work through a collection of items, one at a time.',
    'dictionary': "A collection of key-value pairs.",
    }
for k, v in glossary.items():
    print(f"{k.title()} is a: {v}")

print("Task 6.5")

rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'lena': 'russia',
    'mackenzie': 'canada',
    'yangtze': 'china',
    }

for river, country in rivers.items():
    print(f"{river.title()} flows through {country}")
print("\nThe following rivers are included in this data set:")
for river in rivers.keys():
    print(f'{river.title()}')
print("\nThe following countries are included in this data set:")
for country in rivers.values():
    print(f'{country.title()}')

print("Task 6.6")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

new_users = ['john', 'wendy', 'robert', 'sarah', 'carrol', 'phil', 'estelle']

for new_user in new_users:
    if new_user in favorite_languages.keys():
        print(f"Thank you for taking the poll, {new_users.title()}!")
    else:
        print(f"{new_user.title()}, what's your favorite programming language?")