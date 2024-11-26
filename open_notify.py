import urllib.request
import json

def get_iss_position():
    url = "http://api.open-notify.org/iss-now.json"
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    iss_pos = result['iss_position']
    longitude = iss_pos['longitude']
    latitude = iss_pos['latitude']
    return f"The ISS is currently at Longitude: {longitude}, Latitude: {latitude}"
