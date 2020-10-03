#! python3

print("3.8")
dream_places = ['New Zeland', 'USA', 'Argentina', 'Norway', 'Greenland']
print(dream_places)
print('\n')
print(sorted(dream_places))
print(dream_places)
print(sorted(dream_places, reverse=True))
print(dream_places)
print('\n')
dream_places.reverse()
print(dream_places)
dream_places.reverse()
print(dream_places)
dream_places.sort()
print(dream_places)
dream_places.sort(reverse=True)
print(dream_places)

print("3.8")
print('\n')
names = ['Albert Einstein', 'Julius Cesar', 'Winston Churchill', 'Peter Parker', 'John Snow']
print(len(names))

print("3.8")
print('\n')
mountains = ['Gerlach', 'Sniezka', 'Mount Blanc', 'K2']
print(mountains[0])
print(mountains[1].title())
msg = f"My first pick was a {mountains[1].title()}."
print(msg)
mountains[3] = 'Zugspitze'
print(mountains)
mountains.append('Alt Badia')
print(mountains)
mountains.insert(0, 'Kazbek')
print(mountains)
del mountains[0]
print(mountains)
pop_mountains = mountains.pop(0)
print(f"My favorite pick is a {pop_mountains.title()}.")
mountains.remove('Alt Badia')
print(mountains)
mountains.sort()
print(mountains)
mountains.sort(reverse=True)
print(mountains)
mountains.reverse()
print(mountains)