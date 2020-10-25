#! python3

def make_sandwich(size, *toppings):
    """Information about the prepared sandwich"""
    print(f'\nI am preparing a sandwich of the {size} with toppings: ')
    for topping in toppings:
        print(f"- {topping}")