#! python3

print("2.3")
name = "peter"
print(f"Hello {name.title()}!. Do you want learn Python ")

print("2.4")
name = "peter"
print(name.title())
print(name.upper())
print(name.lower())

print("2.5")
name = "albert einstein"
print(f"{name.title()} once said: 'A person who never made a mistake never tried anything new.'")

print("2.6")
famous_person = "albert einstein"
message = "once said: 'A person who never made a mistake never tried anything new.'"
print(famous_person.title(), message)

print("2.7")
name = "\t Peter Parker \n"
print("Unmodified:")
print(name)

print("\nUsing lstrip():")
print(name.lstrip())

print("\nUsing rstrip():")
print(name.rstrip())

print("\nUsing strip():")
print(name.strip())
