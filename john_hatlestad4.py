import pandas as pd
import matplotlib.pyplot as plt

#Load CSV File
data = pd.read_csv('20220423-Olsen-1.csv')

# Filter Data
zero_runs = data[data['RunsScored'] == 0]['ExitSpeed'].dropna()
runs_scored = data[data['RunsScored'] > 0]['ExitSpeed'].dropna()

# Calculate average exit speed 
zero_runs_average = zero_runs.mean()
runs_scored_average = runs_scored.mean()

x = ['No run scored', 'Run is scored']
y = [zero_runs_average, runs_scored_average]

# Bar Graph
plt.bar(x, y, color=['blue', 'green'])
plt.xlabel('RunsScore')
plt.ylabel('Average ExitSpeed (MPH)')
plt.title('Average ExitSpeed for when run is and isnt scored')
plt.ylim(min(y) - 5, max(y) + 5)
plt.show()