#! python3

print("Task 8.6")

def city_country(city, country):
    """Return a string like 'Santiago, Chile'."""
    return f"{city.title()}, {country.title()}"

city = city_country('santiago', 'chile')
print(city)

city = city_country('london', 'uk')
print(city)

city = city_country('berlin', 'germany')
print(city)

print("Task 8.7")

def make_album(artist, title):
    """Build a dictionary containing information about an album."""
    album_dictionary = {'artist' : artist.title(), 'title' : title.title()}
    return  album_dictionary

album = make_album('shadow', 'imperfect time')
print(album)

album = make_album('larry', 'alone')
print(album)

album = make_album('deck', 'check engine')
print(album)

def make_album(artist, title, tracks = 0):
    """Build a dictionary containing information about an album."""
    album_dictionary = {'artist' : artist.title(), 'title' : title.title()}
    if tracks:
        album_dictionary['tracks'] = tracks
    return  album_dictionary

album = make_album('shadow', 'imperfect time')
print(album)

album = make_album('larry', 'alone', tracks=7)
print(album)

album = make_album('deck', 'check engine', tracks=9)
print(album)

print("Task 8.8")

def make_album(artist, title, tracks = 0):
    """Build a dictionary containing information about an album."""
    album_dictionary = {'artist' : artist.title(), 'title' : title.title()}
    if tracks:
        album_dictionary['tracks'] = tracks
    return  album_dictionary

while True:
    print('\nGive a name of artist.')
    print('\nGive title of album.')
    print('\nGive number of tracks')
    print('\nWrite end to quit program.')

    artist = input('Name: ')
    if artist == 'end':
        break
    title = input('Title: ')
    if title == 'end':
        break
    tracks = input('Number: ')
    if tracks == 'end':
        break

    album = make_album(artist, title, tracks)
    print(album)