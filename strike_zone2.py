import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into a DataFrame
data = pd.read_csv('20220423-Olsen-1.csv')

# Filter data to exclude rows where PlayResult is "Undefined"
filtered_data = data[data['PlayResult'] != 'Undefined'][['PlateLocHeight', 'PlateLocSide', 'PlayResult']]

x = filtered_data['PlateLocSide']
y = filtered_data['PlateLocHeight']

# Create scatter plot
sns.scatterplot(x=x, y=y, hue=filtered_data['PlayResult'])

# Draw strike zone rectangles
plt.axhspan(1.0, 3.0, color='gray', alpha=0.3)
plt.axvspan(-1.0, 1.0, color='gray', alpha=0.3)

# Set labels and title
plt.xlabel('Plate Location (Side)')
plt.ylabel('Plate Location (Height)')
plt.title('Scatter Plot with Strike Zone')

# Show the plot
plt.show()