import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
data = pd.read_csv('20220423-Olsen-1.csv')

# Filter
K_BB = data[data['KorBB'] != 'Undefined']

Stats = K_BB.groupby(['Pitcher', 'KorBB']).size().unstack()

# Bar Graph
ax = Stats.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Number of Strike Outs and Walks each Pitcher had')
plt.xlabel('Pitcher')
plt.ylabel('Number of Occurrences')
plt.legend(title='Key', bbox_to_anchor=(1.0, 1), loc='upper left')  
plt.xticks(rotation=45, ha='right')
plt.show()