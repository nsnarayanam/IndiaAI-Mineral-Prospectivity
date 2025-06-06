
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('/mnt/data/Clustered_NGCM.csv')
fig, axes = plt.subplots(2, 3, figsize=(14, 8))
cols = ['Ni_ppm', 'Co_ppm', 'Cr_ppm', 'U_ppm', 'Au_ppb']

for i, col in enumerate(cols):
    ax = axes[i//3, i%3]
    sns.histplot(df[col], kde=False, ax=ax, color='orange', edgecolor='black')
    ax.set_title(f"{col} Concentration Distribution")
plt.tight_layout()
plt.savefig('/mnt/data/visuals/histograms.png')
