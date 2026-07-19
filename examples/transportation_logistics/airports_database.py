import geopandas as gpd
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from lonboard import Map, ScatterplotLayer

# 1. Download a lightweight, live public dataset (Global Airports)
print("Downloading global airport vector data...")
url = "https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_10m_airports.geojson"
gdf = gpd.read_file(url)

# 2. Extract attribute properties for dynamic styling
# Map the airport 'type' string column to integers so the GPU can parse them
airport_types = gdf["type"].astype("category").cat.codes.to_numpy()

# 3. Create a continuous normalized colormap based on categories
norm = mcolors.Normalize(vmin=airport_types.min(), vmax=airport_types.max())
# FIXED: Using the modern registry lookup instead of the deprecated cm.get_cmap
cmap = plt.colormaps["viridis"]

# Generate an RGBA array (0-255) for every individual feature point
rgba_colors = (cmap(norm(airport_types)) * 255).astype("uint8")

# 4. Construct the Lonboard GPU Scatterplot Layer
layer = ScatterplotLayer.from_geopandas(
    gdf=gdf[["geometry", "name", "type"]],
    get_fill_color=rgba_colors,
    get_radius=15000,          # Base radius in meters
    radius_min_pixels=2,       # Keeps points visible when zoomed way out
    radius_max_pixels=15,      # Prevents clipping overlap when zooming in
    pickable=True              # Allows hovering tooltips out-of-the-box
)

# 5. Instantiate and center the interactive viewport
m = Map(
    layers=[layer],
    view_state={
        "longitude": 0.0,
        "latitude": 20.0,
        "zoom": 1.5,
        "pitch": 0,
        "bearing": 0
    }
)

print("Exporting interactive map canvas to HTML file...")
m.to_html("airport_map.html")

print("Done! Double-click 'airport_map.html' in your file system to view it.")