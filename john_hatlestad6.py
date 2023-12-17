import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file 
data = pd.read_csv('20220423-Olsen-1.csv')

# Filter data
filtered_data = data[data['PlayResult'] != 'Undefined']

x = filtered_data['Distance']
y = filtered_data['HangTime']

# Scatterplot
sns.scatterplot(x=x, y=y, hue=filtered_data['PlayResult'])
plt.xlabel('Distance (Feet)')
plt.ylabel('HangTime (Seconds)')
plt.title('HangTime vs. Distance') 
plt.show()