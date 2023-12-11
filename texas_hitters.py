import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into a DataFrame
data = pd.read_csv('20220423-Olsen-1.csv')

# Filter data for Texas hitters
texas_hitters_valid_results = data[(data['BatterTeam'] == 'TEX_AGG') & (data['PlayResult'] != 'Undefined')]

# Create a bar plot
plt.figure(figsize=(12, 8))
sns.countplot(x='PlayResult', hue='TaggedPitchType', data= texas_hitters_valid_results)
plt.title('Play Result vs. Pitch Type for Texas Hitters')
plt.xlabel('Play Result')
plt.ylabel('Count')
plt.legend(title='Pitch Type')
plt.show()
