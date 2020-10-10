#! python3

print("Task 5.1")
car = 'Peugeot'
print("Is car == 'peugeot'? I predict True.")
print(car == 'Peugeot')

print("\nIs car == 'Peugeot'? I predict False.")
print(car == 'peugeot')

print("\nIs car == 'Peugeot'? I predict True.")
print(car.lower() == 'peugeot')

dog = 'shepard'
print("Is dog == 'shepard'? I predict True.")
print(dog == 'shepard')
print("\nIs dog == 'Shepard'? I predict False.")
print(dog == 'Shepard')

print("Task 5.2")

car = 'Peugeot'
print("\nIs car == 'Peugeot'? I predict False.")
print(car == 'peugeot')

print("\nIs car == 'Peugeot'? I predict True.")
print(car.lower() == 'peugeot')
print('\n')
age = 21
if age == 22:
    print('You can come in!')
else:
    print("You can't come in!")

print('\n')
age = 25
if age >= 22:
    print('You can come in!')
else:
    print("You can't come in!")

print('\n')
age = 25
if age >= 22 and age >=27:
    print('You can come in!')
else:
    print("You can't come in!")

print('\n')
age = 18
if age <= 22 or age >=27:
    print('You can come in!')
else:
    print("You can't come in!")
print('\n')
dogs = ['shepard', 'chow chow', 'york']
print('shepard' in dogs)
print('york' in dogs)
print('amstaf' in dogs)
print('\n')
dogs = ['shepard', 'chow chow', 'york']
name_dog = 'amstaf'
if name_dog not in dogs:
    print("It isn't")
else:
    print("It is")