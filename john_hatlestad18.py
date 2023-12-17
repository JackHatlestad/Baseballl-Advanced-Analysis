import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file 
data = pd.read_csv('20220423-Olsen-1.csv')

# Filter data
pitch_call = data[['PlateLocHeight', 'PlateLocSide', 'PitchCall']]

x = pitch_call['PlateLocSide']
y = pitch_call['PlateLocHeight']

# Scatterplot
sns.scatterplot(x=x, y=y, hue=pitch_call['PitchCall'])
plt.axhspan(1.0, 3.0, color='gray', alpha=0.3)
plt.axvspan(-01.0, 1.0, color='gray', alpha=0.3)
plt.xlabel('X Axis of Strike Zone (Feet)')
plt.ylabel('Y Axis of Strike Zone (Feet)')
plt.title('Strike Zone')
plt.show()