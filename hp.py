import urllib.request
import json
import random

def get_character():
    url = "https://hp-api.herokuapp.com/api/characters"
    request = urllib.request.urlopen(url)
    result = json.loads(request.read())
    char = random.randint(1, 30)
    character_name = result[char]['name']
    is_wizard = result[char].get('wizard', False)
    return f"{character_name} is a wizard" if is_wizard else f"{character_name} is not a wizard"
