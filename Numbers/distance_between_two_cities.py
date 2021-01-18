from haversine import haversine, Unit

#You can use input() for city_a, city_b and unit
city_a = (40.4206213489347, -3.7035801891156064)
city_b = (41.91356287737957, 12.46869592056136)


print(haversine(city_a, city_b, unit=Unit.KILOMETERS))
print(haversine(city_a, city_b, unit=Unit.MILES))

#Also you can connect this programm with Google Maps API (DOWN CODE)

"""
import requests

def distance():
	url = 'https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyC6gnQuMtr3j8szlDvs7XKDAhcrm7NVdrQ'
	r = requests.get(url)
	results = r.json()
	
	print(results)
distance()
"""


