#! python3

print("Task 11.1")

class Employee():

    def __init__(self, first, last, salary):
        self.first = first.title()
        self.last = last.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount

import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
       self.adrian = Employee('adrian', 'szymanski', 50_000)

    def test_give_default_raise(self):
        self.adrian.give_raise()
        self.assertEqual(self.adrian.salary, 55000)

    def test_give_custom_raise(self):
        self.adrian.give_raise(20000)
        self.assertEqual(self.adrian.salary, 70000)


if __name__ == '__main__':
    unittest.main()