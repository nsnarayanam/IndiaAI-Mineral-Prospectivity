
import pandas as pd

df = pd.read_excel('/mnt/data/NGCM-Stream-Sediment-Analysis-Updated.xlsx')
df_clean = df.dropna(subset=['Latitude', 'Longitude', 'U_ppm', 'Ta_ppm', 'Pt_ppb'])
df_clean.to_csv('/mnt/data/Cleaned_NGCM.csv', index=False)
