#! python3

print("Task 6.7")

people = []
person = {
    'first_name': 'john',
    'last_name' : 'dog',
    'age' : '40',
    'city' : 'chicago',
    }
people.append(person)
person = {
    'first_name': 'bety',
    'last_name' : 'cat',
    'age' : '33',
    'city' : 'chicago',
    }
people.append(person)
person = {
    'first_name': 'lila',
    'last_name' : 'shepard',
    'age' : '31',
    'city' : 'boston',
    }
people.append(person)

for person in people:
    name = f"{person['first_name'].title()} {person['last_name'].title()}"
    age = person['age']
    city = person['city'].title()

    print(f"{name} from {city} is {age} years old.")

print("Task 6.8")

pets = []
pet = {
    'animal type': 'dog',
    'name': 'lila',
    'owner': 'Adrian',
    'weight': 43,
    'eats': 'meet',
}
pets.append(pet)

pet = {
    'animal type': 'cat',
    'name': 'bob',
    'owner': 'caty',
    'weight': 4,
    'eats': 'fish',
}
pets.append(pet)

pet = {
    'animal type': 'horse',
    'name': 'draco',
    'owner': 'marry',
    'weight': 90,
    'eats': 'corn',
}
pets.append(pet)

for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print(f"\t{key}: {value}")

print("Task 6.9")

favorite_places = {
    'Igor': ['alaska', 'valencia', 'brazil'],
    'mary': ['russia', 'usa'],
    'wendy': ['spain', 'norway', 'egypt']
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes the following places:")
    for place in places:
        print(f"- {place.title()}")

print("Task 6.10")

persons = {
    'john': ['5', '432'],
    'caty' : ['6', '55'],
    'bob' : ['40', '5' , '53'],
    'lance' : ['2', '5'],
    'wendy' : ['99', '55', '5353', '555'],
    }

for name, numbers in persons.items():
    print(f"\n{name.title()} likes the following number:")
    for number in numbers:
        print(f"- {number.title()}")

print("Task 6.11")

cities = {
    'lodz': {
        'country': 'poland',
        'population': 870_030,
        'nearby mountains': 'tatra',
        },
    'innsbruck': {
        'country': 'austria',
        'population': 345_000,
        'nearby mountains': 'alps',
        },
    'oslo': {
        'country': 'norway',
        'population': 490_000,
        'nearby mountains': 'fiords',
        }
    }

for name_city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    mountains = city_info['nearby mountains'].title()

    print(f"\n{name_city.title()} is in {country.title()}.")
    print(f"  Population: {population}.")
    print(f"  The nearby mountains: {mountains.title()}")

print("Task 6.12")

persons ={}
polling_actives = True

while polling_actives:
    name = input('\tHow are Your name?')
    number = input('\tHow is Your favorite number?')

    persons[name] = number

    repeat = input('Any persons? (yes/no)')
    if repeat == 'no':
        polling_actives = False

for k, v in persons.items():
    print(f"{k.title()} favorite number is: {v}")