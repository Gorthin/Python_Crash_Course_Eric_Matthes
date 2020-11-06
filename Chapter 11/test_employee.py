#! python3

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