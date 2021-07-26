from types import DynamicClassAttribute
import urllib.request

url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_week.geojson"

response = urllib.request.urlopen(url)
data = response.read()

with open("earthquakes.geojson", "wb") as file:
    file.write(data)

    