import geocoder
from utils import str_utils, file_cache

def lookup(location):
    norm_location = str_utils.norm_token(location)
    result = file_cache.get_geo_locations().get(norm_location, {})
    geo_locations = {}
    if not result and norm_location not in file_cache.get_geo_locations() and norm_location:
        g = geocoder.google(norm_location)
        result = g.json if g else {}
        geo_locations[norm_location] = result
        file_cache.update_local_json_cache(geo_locations, 'geo_locations')
    return result