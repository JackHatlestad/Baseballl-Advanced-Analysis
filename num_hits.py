import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv('20220423-Olsen-1.csv')

# Assuming your CSV file has columns like 'BatterTeam' and 'PlayResult'
# Replace these column names with the actual ones in your CSV file
batter_team_column = 'BatterTeam'
play_result_column = 'PlayResult'

# Filter the data for Single, Double, Triple, and HomeRun occurrences
desired_outcomes = ['Single', 'Double', 'Triple', 'HomeRun']
filtered_data = data[data[play_result_column].isin(desired_outcomes)]

# Count occurrences for each BatterTeam and PlayResult combination
result_counts = filtered_data.groupby([batter_team_column, play_result_column]).size().unstack()

# Plot the grouped bar graph
result_counts.plot(kind='bar', width=0.8, figsize=(10, 6), position=1, align='center')

# Adjust x-axis labels
plt.xticks(np.arange(len(result_counts.index)), result_counts.index)

plt.title('Number of Single, Double, Triple, and HomeRun by BatterTeam')
plt.xlabel('BatterTeam')
plt.ylabel('Number of Occurrences')
plt.legend(title='PlayResult', bbox_to_anchor=(1.05, 1), loc='upper left')

# Show the plot
plt.show()