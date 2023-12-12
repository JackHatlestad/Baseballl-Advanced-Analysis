import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV file into a DataFrame
data = pd.read_csv('20220423-Olsen-1.csv')


pitch_counts = data.groupby(['Pitcher', 'TaggedPitchType']).size().unstack(fill_value=0)

# Plotting
pitch_counts.plot(kind='bar', stacked=True, colormap='viridis', figsize=(12, 6))
plt.title('Pitch Types Thrown by Pitcher')
plt.xlabel('Pitcher')
plt.ylabel('Number of Occurrences')
plt.legend(title='Pitch Type', bbox_to_anchor=(1, 1), loc='upper left')
plt.tight_layout()
plt.show()