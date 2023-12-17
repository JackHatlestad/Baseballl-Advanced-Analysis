import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file 
data = pd.read_csv('20220423-Olsen-1.csv')

# Filter 
balls_in_play = data[data['PlayResult'] != 'Undefined']

x = balls_in_play['Distance']
y = balls_in_play['RelSpeed']

# Scatterplot
sns.scatterplot(x=x, y=y, hue=balls_in_play['PlayResult'])
plt.xlabel('Distance (Feet)')
plt.ylabel('RelSpeed (MPH)')
plt.title('RelSpeed vs. Distance')
plt.show()