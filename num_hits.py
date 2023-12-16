import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load CSV File
data = pd.read_csv('20220423-Olsen-1.csv')

batter_team = 'BatterTeam'
play_result = 'PlayResult'

# Filter data 
hits = ['Single', 'Double', 'Triple', 'HomeRun']
filtered_data = data[data[play_result].isin(hits)]

result_counts = filtered_data.groupby([batter_team, play_result]).size().unstack()

# Bar Graph 
result_counts.plot(kind='bar', width=0.8, figsize=(10, 6), position=1, align='center')
plt.xticks(np.arange(len(result_counts.index)), result_counts.index)
plt.title('Number of hits each team had')
plt.xlabel('Team')
plt.ylabel('Number of Occurrences')
plt.legend(title='PlayResult', bbox_to_anchor=(1., 1), loc='upper right')
plt.show()