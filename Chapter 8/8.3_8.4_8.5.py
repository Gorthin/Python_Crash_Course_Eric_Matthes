#! python3

print("Task 8.3")

def make_shirt(size, text):
    """Summarize the shirt that's going to be made."""
    print(f"You ordered a T-shirt with the {size} and '{text}' that will be printed on the T-shirt.")

make_shirt('M', 'I like Python')
make_shirt(text='I like Python', size='M')

print("Task 8.4")

def make_shirt(size = 'L', text = 'I like Python'):
    """Summarize the shirt that's going to be made."""
    print(f"You ordered a T-shirt with the {size} and '{text}' that will be printed on the T-shirt.")

make_shirt()
make_shirt(size= 'M')
make_shirt(text='I learn Python', size='S')

print("Task 8.5")

def describe_city(city, country = 'canada'):
    print(f'Vancouver is located in {country.title()}')

describe_city('ottawa')
describe_city('London', 'UK')
describe_city('Richmond')