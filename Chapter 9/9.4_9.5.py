#! python3

print("Task 9.4")

class Restaurant():
    """Class about opening restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name.title()
        self.cuisine_type = cuisine_type.title()
        self.number_served = 0

    def describe_restaurant(self):
        print(f'My restaurant is {self.restaurant_name} and type food is {self.cuisine_type}')

    def open_restaurant(self):
        print(f'{self.restaurant_name} is open 9 AM.')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, add_served):
        self.number_served += add_served

restaurant = Restaurant('food house', 'grill bar')
restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 430
print(f"Number served: {restaurant.number_served}")

restaurant.number_served = 4245
print(f"Number served: {restaurant.number_served}")

restaurant.number_served = 8900
print(f"Number served: {restaurant.number_served}")

print("Task 9.5")

class User():
    """Represent a user profile."""

    def __init__(self, first_name, last_name, password, email, username, hobby, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.email = email
        self.password = password
        self.username = username
        self.hobby = hobby
        self.location = location.title()
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempst(self):
        self.login_attempts = 0

user1 = User('adam', 'bears', 'a_bear@g.com', 'ursamajor', 'ursa', 'survival', 'Vancouver')
print(user1.describe_user())
user1.greet_user()

print(f"\nLogin attempts: ")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print(f"  Login attempts: {user1.login_attempts}")

print(f"  Reset login attempts:")
user1.reset_login_attempst()
print(f"  Login attempts: {user1.login_attempts}")