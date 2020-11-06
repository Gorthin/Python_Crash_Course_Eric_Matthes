#! python3

def city_country(city, country, population = 0):
    """Return a tex like a Warsaw, Poland - population 1000000"""
    full_info = f"{city.title()}, {country.title()}"
    if population:
        full_info += f" - population {population}"
    return full_info