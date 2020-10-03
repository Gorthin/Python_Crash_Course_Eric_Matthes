#! python3

print("4.3")
for number in range(1,21):
    print(number)
num = [number for number in range(1,21)]
print(num)

print("4.4")
#for number in range(1,1000001):
#    print(number)

#print("4.5")
#numbers = list(range(1, 1_000_001))

#print(min(numbers))
#print(max(numbers))
#print(sum(numbers))

print("4.6")
for number in range(2,21,2):
    print(number)

print("4.7")
threes = list(range(3, 31, 3))

for number in threes:
    print(number)

print("4.8")
cubed = []
for number in range(1,11):
    cubed.append(number**3)
for cube in cubed:
    print(cube)
print("\n")


print("4.9")
num = [number**3 for number in range(1,11)]
print(num)