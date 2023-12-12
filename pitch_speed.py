import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into a DataFrame
data = pd.read_csv('20220423-Olsen-1.csv')

# Assuming 'RelSpeed' is the column containing pitch speeds
# and 'Pitcher' is the column containing pitcher names
pitch_speeds = data['RelSpeed']
pitcher_names = data['Pitcher']

# Combine pitch speeds and pitcher names into a new DataFrame
data = pd.DataFrame({'Pitch Speed': pitch_speeds, 'Pitcher': pitcher_names})

# Set style for better visibility
sns.set(style="whitegrid", font_scale=1.2)

# Create a box plot using seaborn
plt.figure(figsize=(14, 8))
boxplot = sns.boxplot(x='Pitcher', y='Pitch Speed', data=data, palette='viridis')
plt.title('Pitch Speed Distribution by Pitcher', fontsize=16)
plt.xlabel('Pitcher', fontsize=14)
plt.ylabel('Pitch Speed (RelSpeed)', fontsize=14)
plt.xticks(rotation=45, ha='right', fontsize=10)  # Decrease font size of x-axis labels
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the plot
plt.show()