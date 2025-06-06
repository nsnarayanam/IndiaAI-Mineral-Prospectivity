
import geopandas as gpd
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/mnt/data/Clustered_NGCM.csv')
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude), crs="EPSG:4326")

fig, ax = plt.subplots(figsize=(8, 6))
gdf.plot(column='U_ppm', cmap='viridis', legend=True, ax=ax)
plt.title("Uranium (U_ppm) Spatial Distribution")
plt.savefig('/mnt/data/visuals/U_ppm_map.png')
