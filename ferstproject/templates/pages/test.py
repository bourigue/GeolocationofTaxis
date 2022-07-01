import openrouteservice
import folium
client=openrouteservice.Client(key='5b3ce3597851110001cf6248c2e292e64f8440369997bec0ee255a61') # Specify
#your personal API key
coordinates = []
route = client.directions(coordinates=coordinates,
 profile='driving-car',
 format='geojson')
map_directions = folium.Map(location=[33.77, -84.37],
zoom_start=5)
folium.GeoJson(route, name='route').add_to(map_directions)
folium.LayerControl().add_to(map_directions)
map_directions.save("map_directions.html")