import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file
data = pd.read_csv('20220423-Olsen-1.csv')

# Filter data
play_result = data[data['PlayResult'] != 'Undefined'][['PlateLocHeight', 'PlateLocSide', 'PlayResult']]

x = play_result['PlateLocSide']
y = play_result['PlateLocHeight']

# Scatterplot
sns.scatterplot(x=x, y=y, hue=play_result['PlayResult'])
plt.axhspan(1.0, 3.0, color='gray', alpha=0.3)
plt.axvspan(-1.0, 1.0, color='gray', alpha=0.3)
plt.xlabel('X Axis of Strike Zone (Feet)')
plt.ylabel('Y Axis of Strike Zone (Feet)')
plt.title('Strike Zone')
plt.show()