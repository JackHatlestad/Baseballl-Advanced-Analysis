import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('20220423-Olsen-1.csv')

# Filter out rows where 'KorBB' is 'Undefined'
filtered_data = data[data['KorBB'] != 'Undefined']

count_data = filtered_data.groupby(['Pitcher', 'KorBB']).size().unstack()

# Plot a bar chart
count_data.plot(kind='bar', stacked=True, figsize=(10, 6))

plt.title('Occurrence of each KorBB value for each Pitcher')
plt.xlabel('Pitcher')
plt.ylabel('Number of Occurrences')
plt.legend(title='KorBB', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()