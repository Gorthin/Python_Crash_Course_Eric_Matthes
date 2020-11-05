#! python3

print("Task 10.3")

filename = 'guest.txt'

with open(filename, 'w') as f:
    f.write(input("Give me Your name:"))

print("Task 10.4")

filename = 'guest_book.txt'

print("If you want finish write 'q'")
while True:
    name = input('Give me Your name:')
    if name == 'q':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f'{name}\n')
        print(f'Hello {name} you have been added to Guest Book!')

print("Task 10.5")

filename = 'questionnaire.txt'

print('I have a questions about programming.')
print("If you want finish write 'q'")

responses = []
while True:
    question = input('Why do you like a programming?')
    responses.append(question)
    if question == 'q':
        break

with open(filename, 'a') as f:
    for response in responses:
        f.write(f"* {response}\n")
