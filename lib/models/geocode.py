import geocoder
from geocode import geo_locations
from utils import str_utils, init_env

def lookup(location):
    norm_location = str_utils.norm_token(location)
    result = geo_locations.get(norm_location, {})
    if not result and norm_location not in geo_locations and norm_location:
        g = geocoder.google(norm_location)
        result = g.json if g else {}
        geo_locations[norm_location] = result
        init_env.update_location_cache(geo_locations)
    return result