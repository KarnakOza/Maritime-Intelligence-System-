import folium
from shapely import wkt
import asf_search as asf

# ------------------------------------------------
# AOI (Strait of Hormuz)  → WKT uses (lon lat)
# ------------------------------------------------

AOI = 'POLYGON((56.8927 25.962785,54.404297 25.962785,54.404297 27.215486,56.8927 27.215486,56.8927 25.962785))'

# ------------------------------------------------
# Search Sentinel-1 GRDH scenes
# ------------------------------------------------

results = asf.search(
    platform=asf.PLATFORM.SENTINEL1,
    processingLevel='GRD_HD',
    beamMode='IW',
    start='2026-02-21',
    end='2026-03-08',
    intersectsWith=AOI
)

print("Scenes found:", len(results))

# ------------------------------------------------
# Remove duplicate scenes
# ------------------------------------------------

unique = {r.properties["sceneName"]: r for r in results}.values()

print("Unique scenes:", len(unique))

# ------------------------------------------------
# Convert AOI to Folium coordinates (lat, lon)
# ------------------------------------------------

geom = wkt.loads(AOI)
coords = [(y, x) for x, y in geom.exterior.coords]

# ------------------------------------------------
# Create map centered on AOI
# ------------------------------------------------

m = folium.Map(
    location=[26.5,55.5],
    zoom_start=7,
    tiles=None
)

# ------------------------------------------------
# Basemaps
# ------------------------------------------------

folium.TileLayer(
    'OpenStreetMap',
    name='Street Map'
).add_to(m)

folium.TileLayer(
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}',
    attr='Esri',
    name='Satellite'
).add_to(m)

# ------------------------------------------------
# AOI polygon
# ------------------------------------------------

folium.Polygon(
    locations=coords,
    color="red",
    weight=3,
    fill=True,
    fill_opacity=0.2,
    tooltip="AOI"
).add_to(m)

# ------------------------------------------------
# Plot Sentinel-1 scenes
# ------------------------------------------------

for r in unique:

    direction = r.properties["flightDirection"]
    orbit = r.properties["pathNumber"]
    date = r.properties["startTime"]

    # Color by orbit direction
    color = "blue" if direction == "ASCENDING" else "green"

    popup_text = f"""
    <b>Scene:</b> {r.properties['sceneName']} <br>
    <b>Orbit Path:</b> {orbit} <br>
    <b>Direction:</b> {direction} <br>
    <b>Date:</b> {date} <br>
    """

    folium.GeoJson(
        r.geometry,
        style_function=lambda x, col=color: {
            "color": col,
            "weight": 2,
            "fillOpacity": 0.15
        },
        tooltip=r.properties["sceneName"],
        popup=popup_text
    ).add_to(m)

# ------------------------------------------------
# Auto zoom to AOI
# ------------------------------------------------

m.fit_bounds(coords)

# ------------------------------------------------
# Layer control
# ------------------------------------------------

folium.LayerControl().add_to(m)

# ------------------------------------------------
# Display map
# ------------------------------------------------

m
