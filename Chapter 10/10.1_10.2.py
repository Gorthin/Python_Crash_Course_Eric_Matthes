#! python3

print("Task 10.1")

filename = 'learning_python.txt'

print('First solution:')
with open(filename) as f:
    contents = f.read()
print(contents)

print('Second solution:')
with open(filename) as f:
    for line in f:
        print(line.rstrip())

print('Third solution:')
with open(filename) as f:
    lines = f.readlines()

for line in lines:
    print(line.rstrip())

print("Task 10.2")

filename = 'learning_python.txt'

with open(filename) as f:
    lines = f.readlines()

for line in lines:

    line = line.rstrip()
    print(line.replace('Python', 'C'))