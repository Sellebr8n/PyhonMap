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

def color_producer(el):
    if el < 1500:
        return "green"
    elif 1500 <= el < 3500:
        return "orange"
    else:
        return "red"

map = folium.Map(
    location=[38.2, -99.1], 
    zoom_start=5,
    tiles="Stamen Terrain",
)

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el, nm in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (nm, nm, el), width=200, height=100)
    fg.add_child(
        folium.CircleMarker(
            location=[lt,ln],
            radius=3, 
            popup=folium.Popup(iframe),
            color=color_producer(el),
            fill=True,
            fill_color=color_producer(el),
        )
    )

fg.add_child(
    folium.GeoJson(
        data = open('world.json', "r", encoding="utf-8-sig").read(),
        style_function=lambda x: { "fillColor":"green" if x["properties"]["POP2005"] < 10000000 
        else "orange" if 10000000  <= x["properties"]["POP2005"] < 20000000 
        else "red"
        }
    )
)

map.add_child(fg)


map.save("MapAdv.html")