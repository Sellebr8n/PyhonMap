import folium
import pandas

# Check headers =>
# data.columns
data = pandas.read_csv("Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

map = folium.Map(
    location=[38.2, -99.1], 
    zoom_start=5,
    tiles="Stamen Terrain",

)

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=100)
    fg.add_child(
        folium.Marker(
            location=[lt,ln], 
            popup=folium.Popup(iframe),
            icon=folium.Icon(
                color="green"
            )
        )
    )

map.add_child(fg)
map.save("MapAdv.html")