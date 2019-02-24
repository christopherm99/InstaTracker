from geopy.geocoders import Nominatim
geolocator = Nominatim()
def latLon(place):
	location = geolocator.geocode(place)
	return(location.latitude, location.longitude)



