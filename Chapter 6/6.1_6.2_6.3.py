#! python3

print("Task 6.1")

persons = {
    'first_name': 'john',
    'last_name' : 'dog',
    'age' : '40',
    'city' : 'chicago',
    }
print('All information about person:')
print(persons['first_name'])
print(persons['last_name'])
print(persons['age'])
print(persons['city'])

print("Task 6.2")

persons = {
    'john': '5',
    'caty' : '6',
    'bob' : '40',
    'lance' : '2',
    'wendy' : '99',
    }

for k, v in persons.items():
    print(f"{k.title()} favorite number is: {v}")
print('Other solutions:')

persons = {
    'john': '5',
    'caty' : '6',
    'bob' : '40',
    'lance' : '2',
    'wendy' : '99',
    }

num = persons['john']
print(f"John's favorite number is {num}.")

num = persons['caty']
print(f"Caty's favorite number is {num}.")

num = persons['bob']
print(f"Bob's favorite number is {num}.")

num = persons['lance']
print(f"Lance's favorite number is {num}.")

num = persons['wendy']
print(f"Wendy's favorite number is {num}.")

print("Task 6.3")

glossary = {
    'linux' : 'software',
    'variable' : 'value that may vary',
    'zen python' : 'rules of a good python programmer',
    'function range()' : 'generating numbers',
    'lists' : 'a collection of different values',
    }

word = 'linux'
print(f"\n{word.title()}: {glossary[word]}")

word = 'variable'
print(f"\n{word.title()}: {glossary[word]}")

word = 'zen python'
print(f"\n{word.title()}: {glossary[word]}")

word = 'function range()'
print(f"\n{word.title()}: {glossary[word]}")

word = 'lists'
print(f"\n{word.title()}: {glossary[word]}")