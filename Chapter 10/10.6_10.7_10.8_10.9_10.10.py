#! python3

print("Task 10.6")

try:
    x = input("Give me first number: ")
    x = int(x)

    y = input("Give me second number: ")
    y = int(y)
except ValueError:
    print("Give me a number, not a string!")
else:
    add = x + y
    print(add)

print("Task 10.7")

print('Give me a two numbers. I added this numbers.')
print("If you want finish write 'q'")
while True:
    f_num = input('\nFirst number: ')
    if f_num == 'q':
        break
    s_num = input('\nSecond number: ')
    if s_num == 'q':
        break
    try:
        add = int(f_num) + int(s_num)
    except ValueError:
        print('Give me a number, not a string!')
    else:
        print(add)

print("Task 10.8")

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    print(f"\nReading file: {filename}")
    try:
        with open(filename) as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print(f"  Sorry, {filename} don't exist")

print("Task 10.9")

filenames = ['cats.txt', 'dogs.txt']

for filename in filenames:
    try:
        with open(filename) as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        print(f"\nReading file: {filename}")
        print(contents)

print("Task 10.10")

def count_words(filenames, word):
    """Calculating the frequency of occurring words"""
    try:
        with open(filenames, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"  Sorry, {filename} don't exist")
    else:
        words = contents.count(word)
        print(f'File {filename} consists {words} word.')

filenames = ['frankenstein.txt', 'dracula.txt', 'moby_dick.txt', 'alice.txt']
for filename in filenames:
        count_words(filename, 'the')
