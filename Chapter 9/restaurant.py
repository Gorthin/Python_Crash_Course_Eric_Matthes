#! python3

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