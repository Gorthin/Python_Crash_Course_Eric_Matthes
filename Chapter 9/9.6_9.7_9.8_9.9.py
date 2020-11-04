#! python3

print("Task 9.6")

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


class IceCreamStand(Restaurant):
    """Represent Ice Cream Stand"""
    def __init__(self, restaurant_name, cuisine_type = 'ice cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def describe_flavors(self):
        print('We have available flavours:')
        for flavor in self.flavors:
            print(f"* {flavor.title()}")

ice = IceCreamStand('Ice World')
ice.flavors = ['banana', 'vanilla', 'chocolate']

ice.describe_restaurant()
ice.describe_flavors()

print("Task 9.7")

class User():
    """Represent a user profile."""

    def __init__(self, first_name, last_name, password, email, username, hobby, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.password = password
        self.email = email
        self.username = username
        self.hobby = hobby
        self.location = location.title()
        self.login_attempts = 0
        self.privileges = []

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


class Admin(User):
    """Represent a Admin user"""
    def __init__(self, first_name, last_name, password, email, username, hobby, location):
        super().__init__(first_name, last_name, password, email, username, hobby, location)
        self.privileges = []

    def show_privileges(self):
        print('Admin privileges:')
        for privilege in self.privileges:
            print(f"* {privilege.title()}")

adrian = Admin('adrian', 'szymanski', 'zeus', 'adrian88szymanski@gmail.com', 'adrian88szymanski', 'sport', 'poland')
adrian.describe_user()

adrian.privileges = [
    'can add posts',
    'can remove posts',
    'can suspend accounts',
    ]

adrian.show_privileges()

print("Task 9.8")

class User():
    """Represent a user profile."""

    def __init__(self, first_name, last_name, password, email, username, hobby, location):
        """Initialize the user."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.password = password
        self.email = email
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


class Admin(User):
    """Represent a Admin user"""
    def __init__(self, first_name, last_name, password, email, username, hobby, location):
        super().__init__(first_name, last_name, password, email, username, hobby, location)
        self.privileges = Priviliges()


class Priviliges():

    def __init__(self, privileges = []):
        self.privileges = privileges

    def show_privileges(self):
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"* {privilege}")
        else:
            print("- This user has no privileges.")

adrian = Admin('adrian', 'szymanski', 'zeus', 'adrian88szymanski@gmail.com', 'adrian88szymanski', 'sport', 'poland')
adrian.describe_user()

adrian.privileges.show_privileges()

print("\nAdding privileges...")
adrian_privileges = [
    'can add posts',
    'can remove posts',
    'can suspend accounts',
    ]
adrian.privileges.privileges = adrian_privileges
adrian.privileges.show_privileges()

print("Task 9.9")


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def upgrade_baterry(self):
        if self.battery_size == 75:
            self.battery_size == 100
            print("Upgrade baterry to 100 kWh")
        else:
            print('The baterry is upgrade')

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


print("Make an electric car, and check the range:")
my_tesla = ElectricCar('tesla', 'roadster', 2019)
my_tesla.battery.get_range()

print("\nUpgrade the battery, and check the range again:")
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()