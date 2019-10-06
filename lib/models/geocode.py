import geocoder
from utils import str_utils
from models import init_env, geo_locations

def lookup(location):
    norm_location = str_utils.norm_token(location)
    result = geo_locations.get(norm_location, {})
    if not result and norm_location not in geo_locations and norm_location:
        g = geocoder.google(norm_location)
        result = g.json if g else {}
        geo_locations[norm_location] = result
        init_env.update_geo_location_cache(geo_locations)
    return result