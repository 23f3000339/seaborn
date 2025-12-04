import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Re-running with strict dimensions for the user
sns.set_theme(style="white")
sns.set_context("talk")

np.random.seed(42)
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
time_slots = ['09:00', '11:00', '13:00', '15:00', '17:00', '19:00']

data = []
for day in days:
    day_vals = []
    for i, time in enumerate(time_slots):
        val = np.random.randint(20, 50)
        if day in ['Sat', 'Sun']: val += 25
        if i >= 4: val += 15
        day_vals.append(val)
    data.append(day_vals)

df = pd.DataFrame(data, index=days, columns=time_slots)

# Exact dimensions: 8x64 = 512
plt.figure(figsize=(8, 8))

sns.heatmap(
    df, 
    annot=True, 
    fmt="d", 
    cmap="YlGnBu", 
    linewidths=.5, 
    cbar_kws={'label': 'Engagement Score'}
)

plt.title('Customer Engagement Heatmap', pad=20, fontsize=16, fontweight='bold')
plt.xlabel('Time of Day')
plt.ylabel('Day of Week')
plt.tight_layout()

# Save without bbox_inches='tight' to maintain 512x512
plt.savefig('chart.png', dpi=64)
plt.show()
