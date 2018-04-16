import googlemaps
import json


KEY_SEARCH = 'Restaurant'

class GooglePlaces():
    '''
    '''

    def __init__(self):
        print('Google Places')
        self.maps = googlemaps.Client(key='AIzaSyCIPF7mFTSLZOIbuNzVpvYasGRHw70V08g')

    def get_location(self, _place):

        _geocode = self.maps.geocode(_place)
        return _geocode[0]['geometry']['location']

    def get_restaurants(self, _place):

        places = self.maps.places(KEY_SEARCH, 
                                  location=self.get_location(_place),
                                  radius=1500)

        _result = places['results']
        print(_result)
        if _result:
            restaurants = list(map(self.form_features, _result))
            return { 
                     'type': 'FeatureCollection',
                     'features': restaurants
                    }

    def form_features(self, _place):

        name = _place['name']
        _geometry = _place['geometry'] 
        location = _geometry['location']
        icon = _place['icon']

        address = _place['formatted_address']

        _coordinates = list(location.values())
        _coordinates.reverse()
        # _coordinates = list(location.values())
        _form = {
                 'geometry': {
                             'type': 'Point',
                              'coordinates': _coordinates
                            },
                 'type': 'Feature',
                 'properties': {
                                'category': 'restaurant',
                                'hours':'8am - 9:30pm',
                                'address': address,
                                'icon': icon,
                                'name': name,
                                'phone': '00000000000'
                              }
                }

        return _form

if __name__ == '__main__':

    gp = GooglePlaces()
    loc = gp.get_restaurants('Singapore')
    print(loc)
