#! python3

print("Task 11.1")

def city_country(city, country):
    """Return a tex like a Warsaw, Poland"""
    return f"{city.title()}, {country.title()}"

import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    """Test for program name 'city_country'"""
    def test_city_county_name(self):
        formatted_name = city_country('warsaw', 'poland')
        self.assertEqual(formatted_name, 'Warsaw, Poland')

if __name__ == '__main__':
    unittest.main()

print("Task 11.2")

def city_country(city, country, population = 0):
    """Return a tex like a Warsaw, Poland - population 1000000"""
    full_info = f"{city.title()}, {country.title()}"
    if population:
        full_info += f" - population {population}"
    return full_info

import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    """Test for program name 'city_country'"""
    def test_city_county_name(self):
        formatted_name = city_country('warsaw', 'poland')
        self.assertEqual(formatted_name, 'Warsaw, Poland')

    def test_city_county__population_name(self):
        formatted_name = city_country('warsaw', 'poland', 1000000)
        self.assertEqual(formatted_name, 'Warsaw, Poland - population 1000000')

if __name__ == '__main__':
    unittest.main()

