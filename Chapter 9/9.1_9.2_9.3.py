#! python3

print("Task 9.1")

class Restaurant():
    """Class about opening restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()

    def describe_restaurant(self):
        print(f'My restaurant is {self.restaurant_name} and type food is {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open 9 AM.')

restaurant = Restaurant('food house', 'grill bar')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

print("Task 9.2")

class Restaurant():
    """Class about opening restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'My restaurant is {self.restaurant_name} and type food is {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open 9 AM.')

restaurant = Restaurant('food house', 'grill bar')
restaurant.describe_restaurant()

restaurant2 = Restaurant('mango', 'wegge')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('alter ego', 'sandwich')
restaurant3.describe_restaurant()

print("Task 9.3")

class User():
    """Represent a simple user profile."""

    def __init__(self, first_name, last_name, password, email, username, hobby, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.password = password
        self.username = username
        self.hobby = hobby
        self.location = location.title()

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name}")
        print(f"  Email: {self.email}")
        print(f"  Password: {self.password}")
        print(f"  Username: {self.username}")
        print(f"  Hobby: {self.hobby}")
        print(f"  Location: {self.location}")

    def greet_user(self):
        msg = f'Hello {self.first_name} {self.last_name}'
        print(msg)

user1 = User('adam', 'bears', 'a_bear@g.com', 'ursamajor', 'ursa', 'survival', 'Vancouver')
print(user1.describe_user())
user1.greet_user()