
from sklearn.cluster import KMeans
import pandas as pd

df = pd.read_csv('/mnt/data/Cleaned_NGCM.csv')
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(df[['U_ppm', 'Ta_ppm']])
df.to_csv('/mnt/data/Clustered_NGCM.csv', index=False)
