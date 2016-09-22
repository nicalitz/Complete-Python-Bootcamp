'''
Distance Between Two Cities - Calculates the distance between two cities and allows the user to specify a unit
of distance. This program may require finding coordinates for the cities like latitude and longitude.
'''
from geopy.geocoders import Nominatim
from geopy.distance import vincenty

def distance(city1,city2):
    geolocator = Nominatim()
    city1_data = geolocator.geocode(city1)
    city2_data = geolocator.geocode(city2)
    print vincenty((city1_data.latitude,city1_data.longitude),(city2_data.latitude,city2_data.longitude)).kilometers,'km'

distance("Stellenbosch","Somerset West")
