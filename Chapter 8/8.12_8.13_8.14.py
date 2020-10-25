#! python3

print("Task 8.12")

def make_snadwich(size, *toppings):
    """Information about the prepared sandwich"""
    print(f'\nI am preparing a sandwich of the {size} with toppings: ')
    for topping in toppings:
        print(f"- {topping}")

make_snadwich('large', 'pepperoni')
make_snadwich('small', 'pepper', 'cheese', 'onion', 'salami')

print("Task 8.13")

def build_profile(first, last, **user_info):
    """Dictionary with user profile"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return  user_info

user_profile = build_profile('alex', 'ribbon', location='london', field='physics')
user_profile = build_profile('tom', 'ravalon', location='ottawa', field='architect')
print(user_profile)

print("Task 8.14")

def make_car(brand, model, **car_info):
    """Dictionary with car profile"""
    car_info['brand_car'] = brand
    car_info['model_car'] = model
    return  car_info
car = make_car('toyota', 'avensis', color = 'blue', tow_package=True)
print(car)

def make_car(manufacturer, model, **options):
    """Make a dictionary representing a car."""
    car_dict = {
        'manufacturer': manufacturer.title(),
        'model': model.title(),
        }
    for option, value in options.items():
        car_dict[option] = value

    return car_dict

my_outback = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_outback)

my_old_accord = make_car('honda', 'accord', year=1991, color='white',
        headlights='popup')
print(my_old_accord)