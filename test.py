from valmapstats import data

inputs = {"puuid": 'a463de86-a11c-5823-9e32-6a75f8242cdf',
          "game_mode": 'competitive',
          "game_map": 'Ascent',
          "game_region": 'eu'}

matches = data.get_request(**inputs)
import json

# Serialize data into file:
#json.dump( matches, open( "matches.json", 'w' ) )

