#! python3

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
