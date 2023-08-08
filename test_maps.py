import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import json

with open('maps/ascent.json') as user_file:
  file_contents = user_file.read()
map_data = json.loads(file_contents)

with open('matches.json') as user_file:
  file_contents = user_file.read()
match_data = json.loads(file_contents)

image = mpimg.imread("maps/ascent.png")
fig, ax = plt.subplots()
#ax.imshow(image)

#for j in map_data['callouts']:
for i in map_data['callouts']:
    x= i["location"]['x']#*map_data["xMultiplier"] + map_data["xScalarToAdd"]#["x"]
    y=i["location"]['y']#*map_data["yMultiplier"] + map_data["yScalarToAdd"]#["y"]
    ax.scatter(x, y)
    ax.text(x, y, i["regionName"] + i['superRegionName'], va='bottom', ha='left')

for j in match_data["data"][0]["rounds"]:
   if j["plant_events"]["plant_location"] is not None:
      x = j["plant_events"]["plant_location"]['x']
      y = j["plant_events"]["plant_location"]['y']
      ax.plot(x, y, "xg", markersize=10)  # og:shorthand for green circle

for l in match_data["data"][0]["rounds"]:
   for z in l["player_stats"]:
        for k in z["kill_events"]:
            if k["victim_puuid"] == "36b08be2-3dcf-50e0-ae2e-44d9ddc657ad":
                x = k["victim_death_location"]["x"]
                y = k["victim_death_location"]["y"]
                ax.plot(x, y, "xr", markersize=10)  # og:shorthand for green circle

    #plt.legend(loc='upper left', numpoints=1, ncol=3, fontsize=8, bbox_to_anchor=(0, 0))

plt.show()