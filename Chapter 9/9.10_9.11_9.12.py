#! python3

print("Task 9.10")

from restaurant import Restaurant, IceCreamStand

ice = IceCreamStand('Ice World')
ice.flavors = ['banana', 'vanilla', 'chocolate']

ice.describe_restaurant()
ice.describe_flavors()

print("Task 9.11")

from users import Admin

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

print("Task 9.12")

from admin import Admin

adrian = Admin('adrian', 'szymanski', 'zeus', 'adrian88szymanski@gmail.com', 'adrian88szymanski', 'sport', 'poland')
adrian.describe_user()

adrian.privileges.show_privileges()

adrian_privileges = [
    'can add posts',
    'can remove posts',
    'can suspend accounts',
    ]
adrian.privileges.privileges = adrian_privileges

print(f"\nThe admin {adrian.username} has these privileges: ")
adrian.privileges.show_privileges()