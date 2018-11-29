import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'
         
map = folium.Map(location=[38.58, -99.09], zoom_start=6, tiles="Mapbox Bright")
fg = folium.FeatureGroup(name="My map")
#put the latitude and longitude into a list

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius= 6, popup=str(el)+ " m",
    fill_color=color_producer(el), color='black', fill_opacity=0.7))




# for coordinates in [[38.2, -99.1], [39.2, -97.1]]:   #iterating through locations.
#     fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a marker", icon=folium.Icon(color='green')))

map.add_child(fg)   #its good to keep the code organize, 111

map.save("Map1.html")
