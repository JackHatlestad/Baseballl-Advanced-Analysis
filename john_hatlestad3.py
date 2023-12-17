import pandas as pd
import matplotlib.pyplot as plt

# Load CSV File
data = pd.read_csv('20220423-Olsen-1.csv')

# Filter Data 
balls_in_play = data[data['PlayResult'] != 'Undefined']

# Calculate average exit speed for each different type of hit outcome
average_ExitSpeed = balls_in_play.groupby('PlayResult')['ExitSpeed'].mean()

x = average_ExitSpeed.index
y = average_ExitSpeed.values

# bar graph
plt.bar(x, y, color='blue')
plt.xlabel('PlayResult')
plt.ylabel('Average Exit Speed (MPH)')
plt.title('Average Exit Speed for balls in play')
plt.ylim(0, max(y) + 5)
plt.show()