# Project 3
ENGO 551

The purpose of this web application is to add a new map layer to our existing Lab2 web application. Mapbox was used to design and publish the new layer(s).
The 2017 Traffic Incidents dataset was used from Open Calgary. The dataset was saved as a csv file and then loaded into Mapbox as a Tileset. This
Tileset was then added to an existing Mapbox "style". The default "streets" Mapbox style was used because it places emphasis on streets, which are
related to this dataset. This was also the default style used in Lab2. I chose to change the type of the imported Tileset to "symbol" and use a car icon
for the data points in my first layer. I left the default brown colour since it matched the base map style and was easily distinguishable. I left the
opacity at 1 and the size at 1 to ensure the points were easily visible and not overwhelming. I chose to create an additional layer that also added a heatmap
to my first map. This was done by simply loading in the Tileset again and changing its type to "Heatmap". I changed the opacity of this layer to 0.2 to
ensure the base map could still be easily seen underneath.

Updates to Lab2:
index.html - Two additional Mapbox tile layers were added (one for the collision points, and one for the collision points with a heatmap). A layer
toggle was added to the top left corner of the map to choose between these 3 tile layers.
